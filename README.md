# grpc-sandbox

[![Build Status](https://travis-ci.com/KnightWhoSayNi/grpc-sandbox.svg?branch=master)](https://travis-ci.com/KnightWhoSayNi/grpc-sandbox) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/KnightWhoSayNi/grpc-sandbox/blob/master/LICENSE)

## Usage

```shell
docker-compose build
docker-compose up
```

```
Recreating grpc-sandbox_server_1 ... done
Recreating grpc-sandbox_client_1_1 ... done
Recreating grpc-sandbox_client_2_1 ... done
Attaching to grpc-sandbox_server_1, grpc-sandbox_client_1_1, grpc-sandbox_client_2_1
server_1    | Starting server. Listening on port 5000
client_1_1  | 2019-10-20 20:41:53.832657 S <- C: [Alice] Hello World 0
server_1    | 2019-10-20 20:41:53.854774 S <- C: [Alice] Hello World 0
server_1    | 2019-10-20 20:41:53.855235 S -> C: [Echo] HELLO WORLD 0
client_1_1  | 2019-10-20 20:41:53.881134 S -> C: [Echo] HELLO WORLD 0
client_2_1  | 2019-10-20 20:41:53.938486 S <- C: [Bob] Hello World 0
server_1    | 2019-10-20 20:41:53.957453 S <- C: [Bob] Hello World 0
server_1    | 2019-10-20 20:41:53.957628 S -> C: [Echo] HELLO WORLD 0
client_2_1  | 2019-10-20 20:41:53.958541 S -> C: [Echo] HELLO WORLD 0
client_1_1  | 2019-10-20 20:41:54.082422 S <- C: [Alice] Hello World 1
server_1    | 2019-10-20 20:41:54.087200 S <- C: [Alice] Hello World 1
server_1    | 2019-10-20 20:41:54.087299 S -> C: [Echo] HELLO WORLD 1
client_1_1  | 2019-10-20 20:41:54.088156 S -> C: [Echo] HELLO WORLD 1
client_2_1  | 2019-10-20 20:41:54.161530 S <- C: [Bob] Hello World 1
server_1    | 2019-10-20 20:41:54.164850 S <- C: [Bob] Hello World 1
server_1    | 2019-10-20 20:41:54.165076 S -> C: [Echo] HELLO WORLD 1
client_2_1  | 2019-10-20 20:41:54.166524 S -> C: [Echo] HELLO WORLD 1
client_1_1  | 2019-10-20 20:41:54.289487 S <- C: [Alice] Hello World 2
server_1    | 2019-10-20 20:41:54.292826 S <- C: [Alice] Hello World 2
server_1    | 2019-10-20 20:41:54.293130 S -> C: [Echo] HELLO WORLD 2
client_1_1  | 2019-10-20 20:41:54.294202 S -> C: [Echo] HELLO WORLD 2
server_1    | 2019-10-20 20:41:54.371392 S <- C: [Bob] Hello World 2
server_1    | 2019-10-20 20:41:54.371555 S -> C: [Echo] HELLO WORLD 2
client_2_1  | 2019-10-20 20:41:54.367946 S <- C: [Bob] Hello World 2
client_2_1  | 2019-10-20 20:41:54.372082 S -> C: [Echo] HELLO WORLD 2
client_1_1  | 2019-10-20 20:41:54.497225 S <- C: [Alice] Hello World 3
server_1    | 2019-10-20 20:41:54.500021 S <- C: [Alice] Hello World 3
server_1    | 2019-10-20 20:41:54.500175 S -> C: [Echo] HELLO WORLD 3
client_1_1  | 2019-10-20 20:41:54.500910 S -> C: [Echo] HELLO WORLD 3
client_2_1  | 2019-10-20 20:41:54.572823 S <- C: [Bob] Hello World 3
client_2_1  | 2019-10-20 20:41:54.576762 S -> C: [Echo] HELLO WORLD 3
server_1    | 2019-10-20 20:41:54.575450 S <- C: [Bob] Hello World 3
server_1    | 2019-10-20 20:41:54.575635 S -> C: [Echo] HELLO WORLD 3
server_1    | 2019-10-20 20:41:54.708757 S <- C: [Alice] Hello World 4
server_1    | 2019-10-20 20:41:54.708901 S -> C: [Echo] HELLO WORLD 4
client_1_1  | 2019-10-20 20:41:54.706774 S <- C: [Alice] Hello World 4
client_1_1  | 2019-10-20 20:41:54.709690 S -> C: [Echo] HELLO WORLD 4
client_2_1  | 2019-10-20 20:41:54.777729 S <- C: [Bob] Hello World 4
server_1    | 2019-10-20 20:41:54.780526 S <- C: [Bob] Hello World 4
server_1    | 2019-10-20 20:41:54.780676 S -> C: [Echo] HELLO WORLD 4
client_2_1  | 2019-10-20 20:41:54.781935 S -> C: [Echo] HELLO WORLD 4
grpc-sandbox_client_1_1 exited with code 0
grpc-sandbox_client_2_1 exited with code 0
grpc-sandbox_server_1 exited with code 0
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
