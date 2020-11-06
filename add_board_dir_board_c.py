Import("env")

env.Append(BUILD_FLAGS=["-I" + env.GetProjectOption("board_dir")], SRC_FILTER=["+<" + env.GetProjectOption("board_dir") + "/board.c>"])
