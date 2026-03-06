function Invoke-Encode {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, ValueFromPipeline)]
        [AllowEmptyString()]
        [string]$Data
    )

    if ([string]::IsNullOrEmpty($Data)) {
        return ""
    }

    $result = New-Object System.Text.StringBuilder
    $current = $Data[0]
    $count = 1

    for ($i = 1; $i -lt $Data.Length; $i++) {
        if ($Data[$i] -ceq $current) {
            $count++
        }
        else {
            if ($count -gt 1) {
                [void]$result.Append($count)
            }
            [void]$result.Append($current)
            $current = $Data[$i]
            $count = 1
        }
    }

    if ($count -gt 1) {
        [void]$result.Append($count)
    }
    [void]$result.Append($current)

    return $result.ToString()
}

function Invoke-Decode {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, ValueFromPipeline)]
        [AllowEmptyString()]
        [string]$Data
    )

    if ([string]::IsNullOrEmpty($Data)) {
        return ""
    }

    $result = New-Object System.Text.StringBuilder
    $countText = ""

    foreach ($ch in $Data.ToCharArray()) {
        if ([char]::IsDigit($ch)) {
            $countText += $ch
        }
        else {
            $count = if ($countText.Length -gt 0) { [int]$countText } else { 1 }
            $countText = ""

            for ($i = 0; $i -lt $count; $i++) {
                [void]$result.Append($ch)
            }
        }
    }

    return $result.ToString()
}