# UGA (Unified Grocery Application)

# Installation

## How to Install MongoDB for Mac OS (without brew.)

## linked from https://gist.github.com/Sydney-o9/9a6d4a017539cb8610a5695ae505bb61

## 1. Download latest source

````sh
# Get latest from MongoDB website
$ curl -O https://fastdl.mongodb.org/osx/mongodb-osx-x86_64-3.4.6.tgz
$ tar -zxvf mongodb-osx-x86_64-3.4.6.tgz
$ mkdir -p mongodb
$ cp -R -n mongodb-osx-x86_64-3.4.6/ mongodb
$ sudo mv mongodb /usr/local
````

## 2. Configuration

````sh
# Create folder for log files
$ sudo mkdir -p /var/log/mongodb/
# Create folder for database files
$ sudo mkdir -p /var/lib/mongodb/
# Create folder for conf files
$ sudo mkdir -p /etc/mongodb/conf/
# Create main conf file
$ sudo vi /etc/mongodb/conf/mongod.conf
````

Enter the following
````txt
# mongodb.conf

# Where to store the data.

# Note: if you run mongodb as a non-root user (recommended) you may
# need to create and set permissions for this directory manually,
# e.g., if the parent directory isn't mutable by the mongodb user.
dbpath=/var/lib/mongodb

#where to log
logpath=/var/log/mongodb/mongodb.log

logappend=true

#port = 27017

# Disables write-ahead journaling
# nojournal = true

# Enables periodic logging of CPU utilization and I/O wait
#cpu = true

# Turn on/off security.  Off is currently the default
#noauth = true
#auth = true

# Verbose logging output.
#verbose = true

# Inspect all client data for validity on receipt (useful for
# developing drivers)
#objcheck = true

# Enable db quota management
#quota = true

# Set oplogging level where n is
#   0=off (default)
#   1=W
#   2=R
#   3=both
#   7=W+some reads
#diaglog = 0

# Ignore query hints
#nohints = true

# Disable the HTTP interface (Defaults to localhost:28017).
#nohttpinterface = true

# Turns off server-side scripting.  This will result in greatly limited
# functionality
#noscripting = true

# Turns off table scans.  Any query that would do a table scan fails.
#notablescan = true

# Disable data file preallocation.
#noprealloc = true

# Specify .ns file size for new databases.
# nssize = <size>

# Accout token for Mongo monitoring server.
#mms-token = <token>

# Server name for Mongo monitoring server.
#mms-name = <server-name>

# Ping interval for Mongo monitoring server.
#mms-interval = <seconds>

# Replication Options

# in master/slave replicated mongo databases, specify here whether
# this is a slave or master
#slave = true
#source = master.example.com
# Slave only: specify a single database to replicate
#only = master.example.com
# or
#master = true
#source = slave.example.com

# in replica set configuration, specify the name of the replica set
# replSet = setname
````

## 3. Add MongoDB to your Path

Add MongoDB `/bin` folder to your path.

````sh
# MongoDB
export PATH="/usr/local/mongodb/bin:$PATH"
````

## 4. Permissions

We never want to run as super user but create a special daemon `_mongod` for this.

Get the last used GID:

````
# Get the last used GID
$ dscacheutil -q group | grep gid | tail -n 1
gid: 399
# Get list of groups
$ dscl . list /Groups PrimaryGroupID
...
# Get list of groups sorted by ID
$ dscl . list /Groups PrimaryGroupID | tr -s ' ' | sort -n -t ' ' -k2,2
...
````

Therefore, here we will use 400 (make sure it is not taken). 

Please note, on OS X, by convention, all daemon users are prefixed with an underscore, such as `_daemon`.
Before creating a user, we create a group choosing an unused group id:

````
# Create _mongod group
$ sudo dscl . -create /Groups/_mongod
$ sudo dscl . -create /Groups/_mongod PrimaryGroupID 400
````
Once done, we create a new user (we use the same id as we did for the group) - no shell is needed for daemon users:

````
$ sudo dscl . -create /Users/_mongod UniqueID 400
$ sudo dscl . -create /Users/_mongod PrimaryGroupID 400
$ sudo dscl . -create /Users/_mongod UserShell /usr/bin/false
````

Finally, permissions:

````
$ sudo chown -R _mongod:_mongod /var/lib/mongodb/
$ sudo chown -R _mongod:_mongod /var/log/mongodb/
$ sudo chown -R _mongod:_mongod /etc/mongodb/
````
We can now open new terminal and test it works:

````sh
# /we run the command as _mongod to see if it works
$ sudo -u _mongod mongod --config /etc/mongodb/conf/mongod.conf
# show program is running
$ ps aux | grep mongod
# (should show program `mongod` running by `_mongod` daemon user)
````

## 5. Create starting script

We can create a launchctl start script to start `mongod` automatically when starting OS X.

````sh
# MongoDB
sudo vi /Library/LaunchDaemons/mongod.plist
````
Enter the following:

````xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>

    <key>Label</key>
    <string>mongodb</string>

    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/mongodb/bin/mongod</string>
        <string>--config</string>
        <string>/etc/mongodb/conf/mongod.conf</string>
    </array>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>
    
    <key>GroupName</key>
    <string>_mongod</string>
	
    <key>UserName</key>
    <string>_mongod</string>

    <key>WorkingDirectory</key>
    <string>/usr/local/mongodb</string>

    <key>StandardErrorPath</key>
    <string>/var/log/mongodb/error.log</string>

    <key>StandardOutPath</key>
    <string>/var/log/mongodb/output.log</string>

</dict>
</plist>
````

Load launchctl script

````sh
$ sudo launchctl load -w /Library/LaunchDaemons/mongod.plist
$ ps aux | grep mongod
# should now show `mongod` process running
````

## Match a Production environment

````
# Mongo should bring some error messages to your attention which you can fix
$ mongo
`````

- [Fix soft rlimits warnings](https://gist.github.com/tamitutor/6a1e41eec0ce021a9718)
- [Fix Access control is not enabled for the database](https://stackoverflow.com/questions/41615574/mongodb-server-has-startup-warnings-access-control-is-not-enabled-for-the-dat)

## Debug

The following are useful debug commands if needed. 

````sh
# Unload plist file
$ sudo launchctl unload /Library/LaunchDaemons/mongod.plist

# Load plist file
$ sudo launchctl load -w /Library/LaunchDaemons/mongod.plist

# See if plist file is in the list
$ sudo launchctl list | grep mongodb

# Start Mongodb
$ sudo launchctl start mongodb

# Stop Mongodb
$ sudo launchctl stop mongodb

# See if mongod is running
$ ps aux | grep mongod

# See log files
$ cat /var/log/mongodb/mongodb.log
$ cat /var/log/mongodb/error.log
$ cat /var/log/mongodb/output.log

# View System log while launchctl file is loaded and unloaded
$ tail -f /var/log/system.log
````

## References 

https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
https://serverfault.com/questions/183589/how-do-i-activate-launchd-logging-on-os-x
https://github.com/mongodb/mongo/blob/v2.4/debian/mongodb.conf
https://serverfault.com/questions/20702/how-do-i-create-user-accounts-from-the-terminal-in-mac-os-x-10-5
