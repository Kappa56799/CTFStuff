from __future__ import annotations

import pwndbg.gdblib.file
import pwndbg.lib.net


def tcp():
    # For reference, see:
    # https://www.kernel.org/doc/Documentation/networking/proc_net_tcp.txt
    """
    It will first list all listening TCP sockets, and next list all established
    TCP connections. A typical entry of /proc/net/tcp would look like this (split
    up into 3 parts because of the length of the line):
    """
    data = pwndbg.gdblib.file.get("/proc/net/tcp").decode()
    return pwndbg.lib.net.tcp(data)


def unix():
    # We use errors=ignore because of https://github.com/pwndbg/pwndbg/issues/1544
    # TODO/FIXME: this may not be the best solution because we may end up with
    # invalid UDS data. Can this be a problem?
    data = pwndbg.gdblib.file.get("/proc/net/unix").decode(errors="ignore")
    return pwndbg.lib.net.unix(data)


def netlink():
    data = pwndbg.gdblib.file.get("/proc/net/netlink").decode()
    return pwndbg.lib.net.netlink(data)
