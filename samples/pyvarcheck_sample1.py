#Copyright (c) 2026 Benjamin Winter
#This file is part of pyvarcheck which is released under the MIT License.
#See file LICENSE or go to https://github.com/core2000-eU/pyvarcheck for full license details.

#DESCRIPTION
#Easy, high-level var testing for python with auto-conversion features.

#imports
import pyvarcheck

## 
## BASICS
## 

#pyvarcheck does not need initialization and it's functions are called directly.

## 
## RETURN VALUES
## AND
## EXCEPTIONS
## 

#Whenever a check succeeds, every function of *pyvarcheck* returns True. When parameter [convert] is set True, it converts the input item properly and returns it.
#Whenever a check fails, every function of *pyvarcheck* raises Exception type `pyvarcheck.varcheck_exc`.

#Every function of pyvarcheck (for a list, see below) has two additional parameters you can use:
#   exc_prepend     type: STR       description: When the function raises an exception, prepend this string to the exception message
#   exc_append      type: STR       description: When the function raises an exception, append this string to the exception message
#   example: pyvarcheck.str_utf8("my_string", exc_prepend="my_string failed pyvarcheck" , exc_append="some appended text")

## 
## FUNCTIONS AND FEATURES
## 

#check STR for UTF-8 compatibility:
pyvarcheck.str_utf8("my_string") #-> will return True
out = pyvarcheck.str_utf8("my_string",convert=True) #-> out will be "my_string"
try: out = pyvarcheck.str_utf8("invalid code point: \ud800",convert=True) #-> will raise pyvarcheck.pyvarcheck_exc Exception because \ud800 is an invalid UTF-8 code point
except pyvarcheck.pyvarcheck_exc as e: print("str_utf8:"); print(e)

#check input for UUID4 compatibility:
pyvarcheck.uuid4("9d73edfd-a9d1-4041-9abc-335f059f7280") #-> will return True
out = pyvarcheck.uuid4("9d73edfd-a9d1-4041-9abc-335f059f7280",convert=True) #-> out will be type uuid.UUID(9d73edfd-a9d1-4041-9abc-335f059f7280,version=4)
try: out = pyvarcheck.uuid4("1234",convert=True) #-> will raise pyvarcheck.pyvarcheck_exc Exception
except pyvarcheck.pyvarcheck_exc as e: print("uuid4:"); print(e)

#argument name
#enforces for string to be UTF-8 and only contain chars a-z, A-Z, 0-9, _, -, and ,
#enforces max. length of 128 chars, though this can be overwritten.
#enforces for string not to contain any string listed in list [reservedchars], which is empty by default.
pyvarcheck.arg_name("my_arg_name") #-> will return True
out = pyvarcheck.arg_name("my_arg_name",maxlen=64,reservedchars=["#","+","?"],convert=True) #-> out will be "my_arg_name"
try: out = pyvarcheck.arg_name("my*arg*name",maxlen=64,convert=True) #-> will raise pyvarcheck.pyvarcheck_exc Exception
except pyvarcheck.pyvarcheck_exc as e: print("arg_name:"); print(e)

#generic name
#enforces for string to be UTF-8.
#enforces max. length of 128 chars, though this can be overwritten.
#enforces for string not to contain any string listed in list [reservedchars], which is empty by default.
pyvarcheck.generic_name("my generic name") #-> will return True
out = pyvarcheck.generic_name("my generic name",maxlen=64,reservedchars=["#","+","?"],convert=True) #-> out will be "my generic name"
try: out = pyvarcheck.generic_name("my generic name",maxlen=64,reservedchars=[" "],convert=True) #-> will raise pyvarcheck.pyvarcheck_exc Exception because " " is in reservedchars list
except pyvarcheck.pyvarcheck_exc as e: print("generic_name:"); print(e)

#hostname
#enforces for string to be UTF-8 and only contain chars a-z, A-Z, 0-9, _, -, and ,
#enforces max. length of 64 chars, though this can be overwritten.
#enforces for string not to contain any string listed in list [reservedchars], which is empty by default.
pyvarcheck.hostname("computer-hostname") #-> will return True
out = pyvarcheck.hostname("computer-hostname",reservedchars=["#","+","?"],convert=True) #-> out will be "computer-hostname"
try: out = pyvarcheck.hostname("computer-hostname",maxlen=8,convert=True) #-> will raise pyvarcheck.pyvarcheck_exc Exception because [maxlen] is 8
except pyvarcheck.pyvarcheck_exc as e: print("hostname:"); print(e)

#generic description
#enforces for string to be UTF-8.
#enforces max. length of 1024**2 chars, though this can be overwritten.
#enforces for string not to contain any string listed in list [reservedchars], which is empty by default.
#encorces regex match, if given via [re_match] attribute
pyvarcheck.generic_description("my_generic_description_here") #-> will return True
out = pyvarcheck.generic_description("my_generic_description_here",re_match=r"",convert=True) #-> out will be "computer-hostname"
#how to use [re_match]:
try: out = pyvarcheck.generic_description("my*generic*description*here",re_match=r"^[a-zA-Z0-9_.]+$",convert=True) #-> will raise pyvarcheck.pyvarcheck_exc Exception because regex match forbids "*"
except pyvarcheck.pyvarcheck_exc as e: print("generic_description:"); print(e)
try: out = pyvarcheck.generic_description("my_generic_description_here",reservedchars=["_","y"],convert=True) #-> will raise pyvarcheck.pyvarcheck_exc Exception because "_" and "y" are in [reservedchars] list
except pyvarcheck.pyvarcheck_exc as e: print("generic_description:"); print(e)

#IPv4 address
pyvarcheck.ipv4_addr("127.0.0.1") #-> will return True
out = pyvarcheck.ipv4_addr("127.0.0.1",convert=True) #-> out will be type ipaddress.IPv4Address(127.0.0.1)
try: out = pyvarcheck.ipv4_addr("256.0.0.0/24",convert=True) #-> will raise pyvarcheck.pyvarcheck_exc Exception
except pyvarcheck.pyvarcheck_exc as e: print("ipv4_addr:"); print(e)

#IPv6 address
pyvarcheck.ipv6_addr("::1") #-> will return True
out = pyvarcheck.ipv6_addr("::1",convert=True) #-> out will be type ipaddress.IPv6Address(::1)
try: out = pyvarcheck.ipv6_addr("::fffffffffff",convert=True) #-> will raise pyvarcheck.pyvarcheck_exc Exception
except pyvarcheck.pyvarcheck_exc as e: print("ipv6_addr:"); print(e)

#TCP/IP Port
pyvarcheck.tcpip_port(1234) #-> will return True
out = pyvarcheck.tcpip_port(1234,convert=True) #-> out will be int(1234)
try: out = pyvarcheck.tcpip_port(12345678,convert=True) #-> will raise pyvarcheck.pyvarcheck_exc Exception
except pyvarcheck.pyvarcheck_exc as e: print("tcpip_port:"); print(e)

#INT with minimum and maximum value
#first arg is input value (can also be type STR when it is convertible to INT)
#second arg is minimum value (inclusive), must be type INT
#third arg is maximum value (inclusive), must be type INT
pyvarcheck.int_minmax(1234,-10,2000) #-> will return True
out = pyvarcheck.int_minmax("1234",-10,1234,convert=True) #-> out will be int(1234)
try: out = pyvarcheck.int_minmax("one,two,three",-10,2000,convert=True) #-> will raise pyvarcheck.pyvarcheck_exc Exception
except pyvarcheck.pyvarcheck_exc as e: print("int_minmax:"); print(e)

#BOOL
#checks if input data is int(0), int(1), str("0"), str("1"), str("false") or str("true") -> big letters are allowed and are auto-lowered to small letters
pyvarcheck.bool_compatible(0) #-> will return True
out = pyvarcheck.bool_compatible("TRue",convert=True) #-> out will be bool(true)
try: out = pyvarcheck.bool_compatible("false_OR_true_I_cant_decide",convert=True) #-> will raise pyvarcheck.pyvarcheck_exc Exception
except pyvarcheck.pyvarcheck_exc as e: print("bool_compatible:"); print(e)
try: out = pyvarcheck.bool_compatible("troll",convert=True) #-> will raise pyvarcheck.pyvarcheck_exc Exception
except pyvarcheck.pyvarcheck_exc as e: print("bool_compatible:"); print(e)

#That's all! Now go look at some cat pictures.
