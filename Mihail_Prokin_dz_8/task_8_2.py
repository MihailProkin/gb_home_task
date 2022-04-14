import re

PARSE_RE = re.compile(
    r"""(?P<addres>^\S+)[\s-]*\[(?P<datatime>.*)\]\s*\"(?P<resp>\w*)\s*(?P<file>[/\w]+)[^\"]+\"\s+(?P<code>\d+)\s+(?P<size>\d+)""")

with open("./nginx_logs.txt", "r", encoding="utf-8") as file:
    print(*(tuple(x.groupdict().values()) for line in file for x in PARSE_RE.finditer(line)), sep="\n")
