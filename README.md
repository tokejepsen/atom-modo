# atom-modo

Run python scripts from Atom to Modo.

## Features:

* Send an entire file to Modo

## Installation:
Copy from atom-modo.CFG from the setup folder to your configs folder.

Config folder can be found by opening Modo, go to System>Open User Configs Folder

Alternatively you can create the atom-modo.CFG from the following code;

```xml
<?xml version="1.0"?>
<configuration>
  <!-- Executes on startup ( obviously ;] ) -->
  <atom type="StartupCommands">
    <list type="Command">telnet.listen 12357 true</list>
    <list type="Command">log.toConsole</list>
  </atom>

</configuration>
```

## Usage:

Open up a python script and press ```ctrl-alt-r```

## Thanks to:
David Paul Rosser for the original work; https://github.com/davidpaulrosser/atom-maya
