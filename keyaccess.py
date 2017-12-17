#!/usr/bin/python
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import sys
import evdev

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

if len(devices) == 0:
    print "No devices found, try running with sudo"
    sys.exit(1)

try:
    for device in devices:
        if device.name.strip(' ') == 'AB Shutter3':
            print(device)
            device.grab()
            for event in device.read_loop():
                if event.type == evdev.ecodes.EV_KEY:
                   print("%u,%u,%u,%u" % (event.code, event.value, event.sec, event.usec))
except:        
    print("END")
    sys.exit(0)