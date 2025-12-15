function Get-Accumulation {
    param (
        [Parameter(Mandatory)]
        [AllowEmptyCollection()]
        [object[]] $List,

        [Parameter(Mandatory)]
        [scriptblock] $Func
    )

    $result = @()

    foreach ($item in $List) {
        $output = & $Func $item

        if ($output -is [System.Collections.IEnumerable] -and -not ($output -is [string])) {
            foreach ($value in $output) {
                $result += $value
            }
        }
        else {
            $result += $output
        }
    }

    return $result
}
