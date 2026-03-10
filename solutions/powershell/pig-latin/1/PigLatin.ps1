function Invoke-PigLatin {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Text
    )

    function Convert-Word {
        param([string]$Word)

        # Rule 1: starts with vowel, xr, or yt
        if ($Word -match '^(?:[aeiou]|xr|yt)') {
            return $Word + 'ay'
        }

        # Rule 3: consonant cluster followed by qu, or starts with qu
        if ($Word -match '^([^aeiou]?qu)(.+)$') {
            return $matches[2] + $matches[1] + 'ay'
        }

        # Rule 4: consonant(s) followed by y, where y acts as vowel
        if ($Word -match '^([^aeiou]+)(y.+)$') {
            return $matches[2] + $matches[1] + 'ay'
        }

        # Rule 2: initial consonant cluster
        if ($Word -match '^([^aeiou]+)(.+)$') {
            return $matches[2] + $matches[1] + 'ay'
        }

        return $Word + 'ay'
    }

    $words = $Text -split ' '
    $translated = foreach ($word in $words) {
        Convert-Word $word
    }

    return ($translated -join ' ')
}