#Copyright (c) 2026 Benjamin Winter
#This file is part of pyvarcheck which is released under the MIT License.
#See file LICENSE or go to https://github.com/core2000-eU/pyvarcheck for full license details.

#DESCRIPTION
#Easy, high-level var testing for python with auto-conversion features.

#imports
import inspect
import uuid
import ipaddress
import re
import pathlib

#global vars
precomp_regex_1 = re.compile(r"^[a-zA-Z0-9_.]+$") #used often
precomp_regex_2 = re.compile(r"^[a-zA-Z0-9_\-.]+$") #used often
gen_char_limit = 1024**2 #diced; just to have some theoretical yet practical limit

#exception types
class pyvarcheck_exc(Exception):
    def __init__(self,error): super().__init__(error); self.error=error; self.is_exception_from_lib_pyvarcheck=True;
    def __str__(self): return f"{self.error}"

#frontend user-facing functions
def str_utf8(obj_in,convert=False,exc_prepend="",exc_append=""):
    try:
        try:                    _=obj_in.encode("utf-8", errors="strict")
        except Exception as e:  raise pyvarcheck_exc(f"{exc_prepend}cannot encode in UTF-8. *.encode('utf-8', errors='strict') failed with exception {e.__repr__()}{exc_append}")
        if(convert):            return str(obj_in)
        return True
    except Exception as e: helpers.raise_exc_properly(e,inspect.currentframe().f_code.co_name,exc_prepend,exc_append)
def uuid4(obj_in,convert=False,exc_prepend="",exc_append=""):
    try:
        try:                    _=uuid.UUID(obj_in,version=4)
        except Exception as e:  raise pyvarcheck_exc(f"{exc_prepend}cannot convert to UUID. Operation failed with exception {e.__repr__()}{exc_append}")
        if(convert):            return uuid.UUID(obj_in,version=4)
        return True
    except Exception as e: helpers.raise_exc_properly(e,inspect.currentframe().f_code.co_name,exc_prepend,exc_append)
def arg_name(obj_in,maxlen=128,reservedchars=[],convert=False,exc_prepend="",exc_append=""):
    try:
        _=helpers.check_utf8_maxlen_reservedchars(obj_in,gen_char_limit,reservedchars,exc_prepend,exc_append)
        _=helpers.do_regex_match_and_find_err_pos(precomp_regex_2,obj_in,exc_prepend,exc_append)
        if(convert):            return str(obj_in)
        return True
    except Exception as e: helpers.raise_exc_properly(e,inspect.currentframe().f_code.co_name,exc_prepend,exc_append)
def generic_name(obj_in,maxlen=128,reservedchars=[],convert=False,exc_prepend="",exc_append=""):
    try:
        _=helpers.check_utf8_maxlen_reservedchars(obj_in,maxlen,reservedchars,exc_prepend,exc_append)
        if(convert):            return str(obj_in)
        return True
    except Exception as e: helpers.raise_exc_properly(e,inspect.currentframe().f_code.co_name,exc_prepend,exc_append)
def hostname(obj_in,maxlen=64,reservedchars=[],convert=False,exc_prepend="",exc_append=""):
    try:
        _=helpers.check_utf8_maxlen_reservedchars(obj_in,maxlen,reservedchars,exc_prepend,exc_append)
        _=helpers.do_regex_match_and_find_err_pos(precomp_regex_2,obj_in,exc_prepend,exc_append)
        if(convert):            return str(obj_in)
        return True
    except Exception as e: helpers.raise_exc_properly(e,inspect.currentframe().f_code.co_name,exc_prepend,exc_append)
def generic_description(obj_in,maxlen=gen_char_limit,reservedchars=[],re_match=r"",convert=False,exc_prepend="",exc_append=""):
    try:
        _=helpers.check_utf8_maxlen_reservedchars(obj_in,maxlen,reservedchars,exc_prepend,exc_append)
        if(re_match!=r""): _=helpers.do_regex_match_and_find_err_pos(re_match,obj_in,exc_prepend,exc_append) #regex match only when given, it's quite slow
        if(convert):            return str(obj_in)
        return True
    except Exception as e: helpers.raise_exc_properly(e,inspect.currentframe().f_code.co_name,exc_prepend,exc_append)
def ipv4_addr(obj_in,convert=False,exc_prepend="",exc_append=""):
    try:
        try:                    _=ipaddress.IPv4Address(obj_in)
        except Exception as e:  raise pyvarcheck_exc(f"{exc_prepend}not an IPv4 address. ipaddress.IPv4Address(*) failed with exception {e.__repr__()}{exc_append}")
        if(convert):            return ipaddress.IPv4Address(obj_in)
        return True
    except Exception as e: helpers.raise_exc_properly(e,inspect.currentframe().f_code.co_name,exc_prepend,exc_append)
def ipv6_addr(obj_in,convert=False,exc_prepend="",exc_append=""):
    try:
        try:                    _=ipaddress.IPv6Address(obj_in)
        except Exception as e:  raise pyvarcheck_exc(f"{exc_prepend}not an IPv6 address. ipaddress.IPv6Address(*) failed with exception {e.__repr__()}{exc_append}")
        if(convert):            return ipaddress.IPv6Address(obj_in)
        return True
    except Exception as e: helpers.raise_exc_properly(e,inspect.currentframe().f_code.co_name,exc_prepend,exc_append)
def tcpip_port(obj_in,convert=False,exc_prepend="",exc_append=""):
    try:
        try:                                                        obj_in_tmp=int(obj_in)
        except Exception as e:                                      raise pyvarcheck_exc(f"{exc_prepend}expected datatype compatible with (convertible to) [int] but got [{type(obj_in).__qualname__}({obj_in})]{exc_append}")
        if( not obj_in_tmp > 0 ) or ( not obj_in_tmp <= 65535 ):    raise pyvarcheck_exc(f"{exc_prepend}expected TCP/IP Port number in range [1-65535]; to make it clear: (0 ≤ x ≤ 65535, x ∈ ℤ){exc_append}")
        if(convert):                                                return int(obj_in)
        return True
    except Exception as e: helpers.raise_exc_properly(e,inspect.currentframe().f_code.co_name,exc_prepend,exc_append)
def int_minmax(obj_in,value_min,value_max,convert=False,exc_prepend="",exc_append=""):
    try:
        try:                                                                    obj_in_tmp=int(obj_in)
        except Exception as e:                                                  raise pyvarcheck_exc(f"{exc_prepend}expected datatype compatible with (convertible to) [int] but got [{type(obj_in).__qualname__}({obj_in})]{exc_append}")
        if( not obj_in_tmp >= value_min ) or ( not obj_in_tmp <= value_max ):   raise pyvarcheck_exc(f"{exc_prepend}expected integer value between (incl.) [{value_min}] and (incl.) [{value_max}]; to make it clear: ({value_min} ≤ x ≤ {value_max}, x ∈ ℤ){exc_append}")
        if(convert):                                                            return int(obj_in)
        return True
    except Exception as e: helpers.raise_exc_properly(e,inspect.currentframe().f_code.co_name,exc_prepend,exc_append)
def bool_compatible(obj_in,convert=False,exc_prepend="",exc_append=""):
    try:
        dataout=None
        if(isinstance(obj_in,int)):
            _=int_minmax(obj_in,0,1,exc_prepend,exc_append)
            dataout=bool(obj_in)
        elif(isinstance(obj_in,str)):
            _=helpers.check_utf8_maxlen_reservedchars(obj_in,5,[],exc_prepend,exc_append)
            obj_in_tmp = obj_in.lower()
            match obj_in_tmp:
                case "true": dataout=True
                case "false": dataout=False
                case "1": dataout=True
                case "0": dataout=False
                case _: raise pyvarcheck_exc(f"{exc_prepend}expected value convertable to bool. Either integer [0|1] or str ['true'|'false'] but got [{type(obj_in).__qualname__}({obj_in})]{exc_append}")
        else: raise pyvarcheck_exc(f"{exc_prepend}expected datatype either [int] or [str] but got [{type(obj_in).__qualname__}({obj_in})]{exc_append}")
        if(dataout==None): raise Exception(f"unexpected value [None] for var [dataout]. Please report. For debugging: [obj_in]={obj_in}, [exc_prepend]={exc_prepend}, [exc_append]={exc_append}, [convert]={convert}; end of debug")
        if(convert): return bool(dataout)
        return True
    except Exception as e: helpers.raise_exc_properly(e,inspect.currentframe().f_code.co_name,exc_prepend,exc_append)
    
#backend functions
class helpers:
    def check_utf8_maxlen_reservedchars(obj_in,maxlen,reservedchars,exc_prepend,exc_append):
        try:
            pass;                                           _=str_utf8(obj_in,exc_prepend,exc_append)
            if( len(obj_in) > maxlen ):                     raise pyvarcheck_exc(f"{exc_prepend}max length is [{maxlen}] but actual length is [{len(obj_in)}]{exc_append}")
            if( obj_in in reservedchars ):                  raise pyvarcheck_exc(f"{exc_prepend}contains string that is in 'reservedchars' list. 'reservedchars' list is {reservedchars}{exc_append}")
            for i,char in enumerate(obj_in):
                if( char in reservedchars ):
                    char_hex = f"(byte value 0x{char.encode("utf-8",errors="ignore").hex()})";
                    raise pyvarcheck_exc(f"{exc_prepend}contains char {char_hex} at position [{i}] that is in 'reservedchars' list. position is 0-based. 'reservedchars' list is {reservedchars}{exc_append}")
            return True
        except Exception as e: helpers.raise_exc_properly(e,inspect.currentframe().f_code.co_name,exc_prepend,exc_append)
    def do_regex_match_and_find_err_pos(regex_match,obj_in,exc_prepend,exc_append):
        try:
            if( not bool(re.match(regex_match, obj_in)) ):
                for i, char in enumerate(obj_in):
                    if( not bool(re.match(regex_match, char)) ):
                        raise pyvarcheck_exc(f"{exc_prepend}contains invalid char (byte value 0x{char.encode("utf-8",errors="ignore").hex()}) at position [{i}]. re.match(r'{regex_match}') failed. position is 0-based.{exc_append}")
            return True;
        except Exception as e: helpers.raise_exc_properly(e,inspect.currentframe().f_code.co_name,exc_prepend,exc_append)
    def raise_exc_properly(exc,funcname,exc_prepend="",exc_append=""):
        if(isinstance(exc,pyvarcheck_exc)): raise exc
        else:
            tb = exc.__traceback__
            while tb.tb_next:
                tb = tb.tb_next
            line_number = tb.tb_lineno
            absolute_path = pathlib.Path(tb.tb_frame.f_code.co_filename).resolve()
            addl_file_info=f" at file {absolute_path}, line {line_number}"
            raise type(exc)(f"{exc_prepend}lib pyvarcheck: function {funcname}() raised internal Exception {type(exc).__qualname__}('{exc}') {addl_file_info}{exc_append}") from exc #raise the same orig. exception type with prepended message
