# temperature

~~~ { .bash }
#help
./grove_high_accuracy_temperature.py --help
#get temperature 3 times
./grove_high_accuracy_temperature.py -n 3
#get temperature until Ctrl+C pressed
./grove_high_accuracy_temperature.py
~~~

## python code

I2C id change, e.g. id#18 to id#19

I2C address in code

- default I2C id in `/usr/lib/python2.7/dist-packages/upm/pyupm_mcp9808.py` as function parameter `address=0x18`:

~~ { .python }
class MCP9808(_object):
...
    def __init__(self, bus, address=0x18):
        this = _pyupm_mcp9808.new_MCP9808(bus, address)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pyupm_mcp9808.delete_MCP9808
    __del__ = lambda self: None
...
~~

- called by `grove.py/grove/temperature/mcp9808.py`

~~ { .python }
class TemperMCP9808(Temper):
    def __init__(self):
        self.mcp = MCP9808(I2C.MRAA_I2C)
        self.mcp.setMode(True)  # Celsius
        self._resolution = Temper.RES_1_2_CELSIUS
~~

- called by `grove.py/grove/factory/factory.py`

~~ { .python }
def getTemper(self, typ, channel = None):
...
    elif typ == "MCP9808-I2C":
         return TemperMCP9808()
...
~~

- called by `grove.py/grove/grove_high_accuracy_temperature.py`

~~ { .python }
...
sensor = Factory.getTemper("MCP9808-I2C")
...
~~

### trace code for I2C address

- add "trace:"

~~ { .python }
    def __init__(self, bus, address=0x18):
        address=0x19
        print("trace: MCP9808::__init__","address=",address,"(e.g. 0x18 = 24)")
~~

~~ { .text }
grep "trace:" /usr/lib/python2.7/dist-packages/upm/pyupm_mcp9808.py temperature/mcp9808.py factory/factory.py grove_high_accuracy_temperature.py

/usr/lib/python2.7/dist-packages/upm/pyupm_mcp9808.py:
  print("trace: MCP9808::__init__","address=",address,"(e.g. 0x18 = 24)")

temperature/mcp9808.py:
  print("trace: TemperMCP9808::__init__")

python grove_high_accuracy_temperature.py 
Insert Grove - I2C-High-Accuracy-Temperature
  to Grove-Base-Hat any I2C slot
('trace: MCP9808::__init__', 'address=', 25, '(e.g. 0x18 = 24)')
('resolution=', 0.0625)
Detecting temperature...
23.375 Celsius
23.3125 Celsius
...
~~


