def part1() {
    def array = new File("../input.txt") as String[]
    def values = []
    array.each { item ->
        def numbers_in_row = item.findAll( /\d/ )*.toInteger()
        values.add("${numbers_in_row.first()}${numbers_in_row.last()}".toInteger())
    }
    return values*.value.sum()
}

println part1()

def findLesserFirstIndex(String item, String value1, String value2) {
    def index1 = item.indexOf(value1)
    def index2 = item.indexOf(value2)
    if (index1 == -1 && index2 == -1) {
        return -1
    } else if (index1 == -1) {
        return index2
    } else if (index2 == -1) {
        return index1
    } else {
        return index1 < index2 ? index1 : index2
    }
}

def findGreaterLastIndex(String item, String value1, String value2) {
    def index1 = item.lastIndexOf(value1)
    def index2 = item.lastIndexOf(value2)
    if (index1 == -1 && index2 == -1) {
        return -1
    } else if (index1 == -1) {
        return index2
    } else if (index2 == -1) {
        return index1
    } else {
        return index1 > index2 ? index1 : index2
    }
}

def part2() {
    def array = new File("../input.txt") as String[]
    def values = []
    array.each { item ->
        def mapFirstIndex = [
            1: findLesserFirstIndex(item, "1", "one"),
            2: findLesserFirstIndex(item, "2", "two"),
            3: findLesserFirstIndex(item, "3", "three"),
            4: findLesserFirstIndex(item, "4", "four"),
            5: findLesserFirstIndex(item, "5", "five"),
            6: findLesserFirstIndex(item, "6", "six"),
            7: findLesserFirstIndex(item, "7", "seven"),
            8: findLesserFirstIndex(item, "8", "eight"),
            9: findLesserFirstIndex(item, "9", "nine"),
        ]
        def mapLastIndex = [
            1: findGreaterLastIndex(item, "1", "one"),
            2: findGreaterLastIndex(item, "2", "two"),
            3: findGreaterLastIndex(item, "3", "three"),
            4: findGreaterLastIndex(item, "4", "four"),
            5: findGreaterLastIndex(item, "5", "five"),
            6: findGreaterLastIndex(item, "6", "six"),
            7: findGreaterLastIndex(item, "7", "seven"),
            8: findGreaterLastIndex(item, "8", "eight"),
            9: findGreaterLastIndex(item, "9", "nine"),
        ]

        mapFirstIndex.removeAll {it -> it.value == -1}
        mapFirstIndex = mapFirstIndex.sort {it.value}

        mapLastIndex.removeAll {it -> it.value == -1}
        mapLastIndex = mapLastIndex.sort {it.value}

        values.add("${mapFirstIndex.keySet().first()}${mapLastIndex.keySet().last()}".toInteger())
    }
    return values*.value.sum()
}

println part2()
