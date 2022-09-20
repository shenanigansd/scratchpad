Attribute VB_Name = "PageBreakModule"
Sub InsertPageBreaks()
Dim xLastRow As Long
Dim xWs As Worksheet
Set xWs = Application.ActiveSheet
xRow = Application.InputBox("Row", xTitleId, "", Type:=1)
xWs.ResetAllPageBreaks
xLastRow = xWs.Range("A1").SpecialCells(xlCellTypeLastCell).Row
For i = xRow + 1 To xLastRow Step xRow
    xWs.HPageBreaks.Add Before:=xWs.Cells(i, 1)
Next
End Sub
