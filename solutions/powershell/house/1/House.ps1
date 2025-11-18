function Get-Rhyme {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [int]$Start,

        [Parameter(Mandatory)]
        [int]$End
    )

    # Ordered subjects
    $subjects = @(
        "the house that Jack built",
        "the malt",
        "the rat",
        "the cat",
        "the dog",
        "the cow with the crumpled horn",
        "the maiden all forlorn",
        "the man all tattered and torn",
        "the priest all shaven and shorn",
        "the rooster that crowed in the morn",
        "the farmer sowing his corn",
        "the horse and the hound and the horn"
    )

    # Ordered verbs
    $verbs = @(
        "",  # verse 1 uses no verb
        "lay in",
        "ate",
        "killed",
        "worried",
        "tossed",
        "milked",
        "kissed",
        "married",
        "woke",
        "kept",
        "belonged to"
    )

    # Build a single verse based on number (1–12)
    function Build-Verse([int]$n) {
        # Start line
        $line = "This is $($subjects[$n - 1])"

        # Add cumulative lines (from n-1 down to 1)
        for ($i = $n - 1; $i -gt 0; $i--) {
            $line += " that $($verbs[$i]) $($subjects[$i - 1])"
        }

        return "$line."
    }

    # Build full output (one or multiple verses)
    $output = for ($v = $Start; $v -le $End; $v++) {
        Build-Verse $v
    }

    # When multiple verses, join with newlines
    return ($output -join "`n")
}
