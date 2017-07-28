from argparse import ArgumentParser
import socket


def _hostname():
    return socket.gethostname().split('.')[0]


def parse_cmdline_glusterd(args):
    return {
        "name": "glusterd",
        "hostname": _hostname()
    }


def parse_cmdline_glusterfsd(args):
    parser = ArgumentParser()
    parser.add_argument("-s", dest="server")
    parser.add_argument("--volfile-id")
    parser.add_argument("--brick-name")
    pargs, unknown = parser.parse_known_args(args)

    return {
        "name": "glusterfsd",
        "hostname": _hostname(),
        "server": pargs.server,
        "brick_path": pargs.brick_name,
        "volname": pargs.volfile_id.split(".")[0]
    }


def parse_cmdline_glustershd(args):
    # TODO: Parsing
    pass


def parse_cmdline_python(args):
    if len(args) > 1 and "glustereventsd" in args[1]:
        return parse_cmdline_glustereventsd(args)
    elif len(args) > 1 and "gsyncd" in args[1]:
        return parse_cmdline_gsyncd(args)


def parse_cmdline_gsyncd(args):
    data = {
        "name": "gsyncd",
        "hostname": _hostname()
    }
    if "--feedback-fd" in args:
        data["role"] = "worker"
    elif "--agent" in args:
        data["role"] = "agent"
    elif "--monitor" in args:
        data["role"] = "monitor"
    elif "--listen" in args:
        data["role"] = "slave"

    return data


def parse_cmdline_glustereventsd(args):
    return {
        "name": "glustereventsd",
        "hostname": _hostname()
    }
