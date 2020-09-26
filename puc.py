# Prefix Unit Converter
import sys

bases = [ "hz", "b", "s", "B" ]
prefixes = { "p":1e-12, "n":1e-9, "u":1e-6, "m":1e-3, "k":1e3, "M":1e6, "G":1e9, "":1 }
power_prefixes = { "k":1024, "M":pow(1024,2), "G":pow(1024,3), "":1 }


# "to" text is ignored

whoami = sys.argv[0]

from_val  = ""
from_unit = ""
to_unit   = ""

from_prefix = ""
to_prefix = ""

try:
    to_unit   = sys.argv.pop()
    from_unit = sys.argv.pop()
    if from_unit.lower() == "to":
        from_unit = sys.argv.pop()
    from_val  = sys.argv.pop()
except:
    print("Usage: " + whoami + " <from value> <from unit> [to] <to unit>")

# extract base and prefix

for prefix in prefixes.keys():
    # skip blanks
    if len(prefix) == 0:
        continue
    if from_unit.startswith(prefix,0,1):
        from_prefix = prefix
    if to_unit.startswith(prefix,0,1):
        to_prefix = prefix

from_base = from_unit[len(from_prefix):]
to_base   = to_unit[len(to_prefix):]

if (from_base.lower() == "hz" and to_base == "s") or (from_base == "s" and to_base.lower() == "hz"):
    # calculate a period
    to_val = (1/prefixes[to_prefix]) * (1 / (float(from_val) * prefixes[from_prefix]))
    # calculate a period
elif (from_base[0] == "b" and to_base[0] == "B"): # /8
    to_val = (prefixes[from_prefix])*float(from_val)
    to_val /= float(8*power_prefixes[to_prefix])
elif (from_base[0] == "B" and to_base[0] == "b"): # x8
    to_val = (8*power_prefixes[from_prefix])*float(from_val)
    to_val /= float(prefixes[to_prefix])
else:
    to_val = (float(from_val) * prefixes[from_prefix]) / prefixes[to_prefix]


print(str(from_val) + " " + str(from_unit) + " is " + str(to_val) + " " + str(to_prefix) + str(to_base))
