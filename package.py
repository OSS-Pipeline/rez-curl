name = "curl"

version = "7.66.0"

authors = [
    "Daniel Stenberg"
]

description = \
    """
    Curl is a command-line tool for transferring data specified with URL syntax.
    """

requires = [
    "cmake-3+",
    "gcc-6+",
    "zlib-1.2+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "curl"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "curl-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    # Helper environment variables.
    env.CURL_BINARY_PATH.set("{root}/bin")
    env.CURL_INCLUDE_PATH.set("{root}/include")
    env.CURL_LIBRARY_PATH.set("{root}/lib")
