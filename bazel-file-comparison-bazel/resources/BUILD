load("@bzlws//rules:bzlws_copy.bzl", "bzlws_copy")

bzlws_copy(
    name = "copy_resources",
    out = "resources/{FILENAME}",
    force = True,
    tags = ["manual"],
    srcs = [
        "test-file1.txt","test-file2.txt"
    ],
)
