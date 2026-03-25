function Invoke-Append {
    param(
        $List1,
        $List2
    )

    $result = @()

    foreach ($item in $List1) {
        $result += $item
    }

    foreach ($item in $List2) {
        $result += $item
    }

    return $result
}

function Invoke-Concatenate {
    param(
        $Lists
    )

    $result = @()

    foreach ($list in $Lists) {
        foreach ($item in $list) {
            $result += ,$item
        }
    }

    return $result
}

function Invoke-Filter {
    param(
        $List,
        $Predicate
    )

    $result = @()

    foreach ($item in $List) {
        if (& $Predicate $item) {
            $result += $item
        }
    }

    return $result
}

function Get-Length {
    param(
        $List
    )

    $count = 0

    foreach ($item in $List) {
        $count++
    }

    return $count
}

function Invoke-Map {
    param(
        $List,
        $Function
    )

    $result = @()

    foreach ($item in $List) {
        $result += (& $Function $item)
    }

    return $result
}

function Invoke-Foldl {
    param(
        $Function,
        $List,
        $Accumulator
    )

    $acc = $Accumulator

    foreach ($item in $List) {
        $acc = & $Function $acc $item
    }

    return $acc
}

function Invoke-Foldr {
    param(
        $Function,
        $List,
        $Accumulator
    )

    $acc = $Accumulator

    # manual reverse iteration (no built-ins)
    $temp = @()
    foreach ($item in $List) {
        $temp = ,$item + $temp
    }

    foreach ($item in $temp) {
        $acc = & $Function $acc $item
    }

    return $acc
}

function Invoke-Reverse {
    param(
        $List
    )

    $result = @()

    foreach ($item in $List) {
        $result = ,$item + $result
    }

    return $result
}