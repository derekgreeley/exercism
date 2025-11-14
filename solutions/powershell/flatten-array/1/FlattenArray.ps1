function Invoke-FlattenArray {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [object]$Array
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        # Use a List for efficient appends
        $result = [System.Collections.Generic.List[object]]::new()

        function Add-Flat {
            param([object]$Node)

            if ($null -eq $Node) { return }

            if ($Node -is [System.Array]) {
                foreach ($item in $Node) {
                    Add-Flat -Node $item
                }
            } else {
                [void]$result.Add($Node)
            }
        }

        Add-Flat -Node $Array

        # Ensure the function always returns an array (even when empty)
        ,$result.ToArray()
    }
}
