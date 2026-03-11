function Get-LineUp {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Name,

        [Parameter(Mandatory)]
        [int]$Number
    )

    # Handle 11–13 exception
    $lastTwo = $Number % 100

    if ($lastTwo -ge 11 -and $lastTwo -le 13) {
        $suffix = "th"
    }
    else {
        switch ($Number % 10) {
            1 { $suffix = "st" }
            2 { $suffix = "nd" }
            3 { $suffix = "rd" }
            default { $suffix = "th" }
        }
    }

    return "$Name, you are the $Number$suffix customer we serve today. Thank you!"
}