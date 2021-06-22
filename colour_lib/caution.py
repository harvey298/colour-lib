# 
# Copyright harvey298 2021 GPL
#
from .main import merge_format, format_reset
import sys
def caution(warning):
    print(merge_format("bold", "yellow")+"[CAUTION] "+format_reset(2)+warning+format_reset(0))

def error(error,status = 0):
    print(merge_format("bold", "red")+"[ERROR] "+format_reset(2)+str(error)+format_reset(0))
    if status == 0:
        return
    else:
        sys.exit(status)

def info(info):
    print(merge_format("bold", "blue")+"[INFO] "+format_reset(2)+str(info)+format_reset(0))
