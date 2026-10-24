# pyvarcheck  
Easy, high-level var testing for python with auto-conversion features.  

Test INT, STR, BYTEARRAY, BOOL, and many other data types for your requirements and auto-convert them.  
There's pre-defined functions to match strings for hostnames, arguments, IP addresses, ports and many more. *pyvarcheck* tells you the index of a failed regex match.  

> [!NOTE]
> This project is in use by **MPSS - Multi-platform shared storage**, a brand-new way to combine, share and access storage over LAN and WAN. Run servers, workstations and clients, multiple OSs and huge numbers of devices simultaneously.  
[Take a look here if that sounds interesting! \[core2000.com\]](https://core2000.com/software/mpss/)  

[Supporters](#now-for-the-boring-part) and contributors are welcome any day of the week :)

## Fast track
Install with `pip install pyvarcheck`; import into your project with `import pyvarcheck`; then open and run example file [`/samples/pyvarcheck_sample1.py`](https://github.com/core2000-eU/pyvarcheck/blob/main/samples/pyvarcheck_sample1.py) from GitHub.  

## Documentation
For documentation, please use the example file [`/samples/pyvarcheck_sample1.py`](https://github.com/core2000-eU/pyvarcheck/blob/main/samples/pyvarcheck_sample1.py) from GitHub.  
Everything's neatly documented in there.  

- Whenever a check succeeds, every function of *pyvarcheck* returns True. When parameter [convert] is set True, it converts the input item properly and returns it.  
- Whenever a check fails, every function of *pyvarcheck* raises Exception type `pyvarcheck.varcheck_exc`.  
- On the occasion that there's a programmatic error in any *pyvarcheck* function (sorry, my bad), *pyvarcheck* raises the original exception to the caller. Feel free to report such occasions.  

## Basics
**Compatibility**  in short: any platform on Python 3.10+.  OS-independent.  
**Status:** *public beta*. Should work without issues, waiting for community response before releasing final v1.  
**Built** on W11 25H2 with python 3.15.0, pip 26.2.2, build 1.6.1, twine 7.0.0. Standard settings.

## Build from source
The library is built witout any special options - as per the pypi manual. It uses `setuptools` (`setup.py`) and not the toml file.  
- change into the library source code root folder
- python3 -m build
- I recommend you use a venv for this proceduce, and alter the `py -m build` command accordingly.  

## Official Sources

  | Site | URL |
  |------|---------|
  | **GitHub** | [github.com/core2000-eU/pyvarcheck](https://github.com/core2000-eU/pyvarcheck) |
  | **pypi.org** | [pypi.org/project/pyvarcheck](https://pypi.org/project/pyvarcheck) |
  | core2000.com (Website/info only, no release) | [core2000.com/software](https://core2000.com/software/) |

## Now for the boring part
**This library is created and maintained free of cost by a real human being /bla /bla /bla ...** You know the deal by now.  
But seriously, monetary support a serious subject and without some income, I cannot continue to publish and maintain.  

Not that anyone needs my gibberish anyways, but if you find it helpful, **please consider the below. Thanks :)**  
--> [**buymeacoffee.com/core2000**](https://buymeacoffee.com/core2000)

## About
Created on 10.2026 and happily maintained since by **core2000** and it's owner, Benjamin Winter.  
For more details, you can pay us a visit over on [**core2000.com**](https://core2000.com/).
