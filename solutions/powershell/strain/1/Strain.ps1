function Invoke-Keep {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [AllowEmptyCollection()]
        [object[]]$Data,

        [Parameter(Mandatory, Position=1)]
        [scriptblock]$Predicate
    )

    process {
        $out = [System.Collections.Generic.List[object]]::new()
        foreach ($item in $Data) {
            if (& $Predicate $item) {
                [void]$out.Add($item)
            }
        }
        ,$out.ToArray()
    }
}

function Invoke-Discard {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [AllowEmptyCollection()]
        [object[]]$Data,

        [Parameter(Mandatory, Position=1)]
        [scriptblock]$Predicate
    )

    process {
        $out = [System.Collections.Generic.List[object]]::new()
        foreach ($item in $Data) {
            if (-not (& $Predicate $item)) {
                [void]$out.Add($item)
            }
        }
        ,$out.ToArray()
    }
}
