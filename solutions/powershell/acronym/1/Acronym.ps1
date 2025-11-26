function Get-Acronym {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Phrase
    )

    # Treat hyphens as word separators
    $normalized = $Phrase -replace '-', ' '

    # Remove all non-letter characters except spaces
    # (commas, apostrophes, underscores, punctuation, etc. are stripped)
    $normalized = $normalized -replace '[^A-Za-z ]', ''

    # Split into words, ignoring any empty entries from multiple spaces
    $words = $normalized -split '\s+' | Where-Object { $_ -ne '' }

    # Take the first character of each word, uppercase it, and join
    $acronym = ($words | ForEach-Object { $_[0].ToString().ToUpper() }) -join ''

    return $acronym
}
