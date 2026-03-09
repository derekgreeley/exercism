function Invoke-Counter {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [int]$Value
    )

    $count = 0

    while ($Value -gt 0) {
        # Check if the least significant bit is 1
        if (($Value -band 1) -eq 1) {
            $count++
        }

        # Shift right by 1 bit
        $Value = $Value -shr 1
    }

    return $count
}