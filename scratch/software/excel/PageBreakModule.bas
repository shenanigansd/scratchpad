Attribute VB_Name = "PageBreakModule"
Sub InsertPageBreaks()
'Updateby20140618
Dim xLastrow As Long
Dim xWs As Worksheet
Set xWs = Application.ActiveSheet
xRow = Application.InputBox("Row", xTitleId, "", Type:=1)
xWs.ResetAllPageBreaks
xLastrow = xWs.Range("A1").SpecialCells(xlCellTypeLastCell).Row
For i = xRow + 1 To xLastrow Step xRow
    xWs.HPageBreaks.Add Before:=xWs.Cells(i, 1)
Next
End Sub
