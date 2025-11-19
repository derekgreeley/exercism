function Invoke-MicroBlog {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position = 0)]
        [string]$InputString
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        # Use .NET's StringInfo to enumerate Unicode text elements (grapheme clusters)
        $enumerator = [System.Globalization.StringInfo]::GetTextElementEnumerator($InputString)

        $result = New-Object System.Text.StringBuilder
        $count  = 0

        while ($enumerator.MoveNext() -and $count -lt 5) {
            [void]$result.Append($enumerator.Current)
            $count++
        }

        $result.ToString()
    }
}
        