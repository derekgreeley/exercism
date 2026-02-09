function Invoke-TwelveDays {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [int] $Start,

        [Parameter(Mandatory)]
        [int] $End
    )

    $ordinals = @(
        $null,
        "first","second","third","fourth","fifth","sixth",
        "seventh","eighth","ninth","tenth","eleventh","twelfth"
    )

    $gifts = @(
        $null,
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, and a Partridge in a Pear Tree.",
        "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
    )

    $verses = New-Object System.Collections.Generic.List[string]

    for ($day = $Start; $day -le $End; $day++) {
        $verses.Add("On the $($ordinals[$day]) day of Christmas my true love gave to me: $($gifts[$day])")
    }

    return ($verses -join "`n")
}
