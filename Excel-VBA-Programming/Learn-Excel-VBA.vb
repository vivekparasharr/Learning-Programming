'https://www.excel-easy.com/vba/create-a-macro.html

Option Explicit

'This is a comment

Sub simple_hello()
'Add Hello to cell A2
Range("A2").Value = "Hello"
Worksheets("Sheet1").Range("B2").Value = "Hello"
Worksheets(1).Range("C2").Value = "Hello"
'Show a simple message
MsgBox "I added Hello in cell A2, B2 and C2"
End Sub

Sub interactive_hello()
'Show an interactive message
MsgBox "Hello " & Range("C5").Value & vbNewLine & "So you are " & Range("C6") & " years old!"
End Sub

Sub how_many_worksheets()
MsgBox Worksheets.Count
End Sub

Sub how_range_works()
Range("F1:F4").Value = 5
Range("G1:G4,H1:H4").Value = 10

'Note: to refer to a named range in your Excel VBA code, use a code line like this:
'Range("Prices").Value = 15

'Instead of Range, you can also use Cells. Using Cells is particularly useful when you want to loop through ranges.
'Cells(3, 2).Value = 2
'Range(Cells(1, 1), Cells(4, 1)).Value = 5
End Sub

'You can declare a Range object by using the keywords Dim and Set.
'Dim example As Range
'Set example = Range("A1:C4")
'Can assign value to object using .Value
'example.Value = 8

'An important method of the Range object is the Select method. The Select method simply selects a range.
'Dim example As Range
'Set example = Range("A1:C4")
'Can assign value to object using .Select
'example.Select

'Note: to select cells on a different worksheet, you have to activate this sheet first. For example, the following code lines select cell B7 on the third worksheet from the left.

'The Rows property gives access to a specific row of a range.
'Dim example As Range
'Set example = Range("A1:C4")
'Select row using Rows(x).Select
'example.Rows(3).Select
'example.Columns(2).Select

'The Copy and Paste method are used to copy a range and to paste it somewhere else on the worksheet.
'Range("A1:A2").Select
'Selection.Copy
'Range("C3").Select
'ActiveSheet.Paste

'Although this is allowed in Excel VBA, it is much better to use the code line below which does exactly the same.
'Range("C3:C4").Value = Range("A1:A2").Value

'To clear the content of an Excel range, you can use the ClearContents method.
'Range("A1").ClearContents
'or
'Range("A1").Value = ""

'With the Count property, you can count the number of cells, rows and columns of a range.
'Dim example As Range
'Set example = Range("A1:C4")
'MsgBox example.Count

'or

'Dim example As Range
'Set example = Range("A1:C4")
'MsgBox example.Rows.Count


Variables
Dim x As Integer
x = 6
Range("A1").Value = x

Dim book As String
book = "bible"
Range("A1").Value = book

Dim x As Integer
x = 5.5
MsgBox "value is " & x

Dim x As Double
x = 5.5
MsgBox "value is " & x

Dim continue As Boolean
continue = True
If continue = True Then MsgBox "Boolean variables are cool"


'If Then Statement
Dim score As Integer, result As String
score = Range("A1").Value

If score >= 60 Then result = "pass"

Range("B1").Value = result


Dim score As Integer, result As String
score = Range("A1").Value

'If Else Statement
If score >= 60 Then
    result = "pass"
Else
    result = "fail"
End If

Range("B1").Value = result

'Select Case
'First, declare two variables. One variable of type Integer named score and one variable of type String named result
Dim score As Integer, result As String
'We initialize the variable score with the value of cell A1
score = Range("A1").Value
'Add the Select Case structure
Select Case score
    Case Is >= 80
        result = "very good"
    Case Is >= 70
        result = "good"
    Case Is >= 60
        result = "sufficient"
    Case Else
        result = "insufficient"
End Select
'Write the value of the variable result to cell B1
Range("B1").Value = result


'Delete Blank Cells
'1. First, we declare two variables of type Integer. One named counter and one named i. We initialize the variable counter with value 0.
Dim counter As Integer, i As Integer
counter = 0
'2. Next, we check for each cell whether it is empty or not (<> means not equal to). We are using a loop for this. If not empty, we write the value to column B. The counter holds track of the number of cells that have been copied to column B. Each time we copy a value to column B, we increment counter by 1. This piece of the program looks as follows:
For i = 1 To 10
    If Cells(i, 1).Value <> "" Then
        Cells(counter + 1, 2).Value = Cells(i, 1).Value
        counter = counter + 1
    End If
Next i
'3. Finally, we empty Range("A1:A10"), copy the values of column B to column A, and empty Range("B1:B10").
Range("A1:A10").Value = ""
Range("A1:A10").Value = Range("B1:B10").Value
Range("B1:B10") = ""


'Loop
'Single Loop
Dim i As Integer

For i = 1 To 6
    Cells(i, 1).Value = 100
Next i

'Double Loop
Dim i As Integer, j As Integer

For i = 1 To 6
    For j = 1 To 2
        Cells(i, j).Value = 100
    Next j
Next i

'Triple Loop
Dim c As Integer, i As Integer, j As Integer

For c = 1 To 3
    For i = 1 To 6
        For j = 1 To 2
            Worksheets(c).Cells(i, j).Value = 100
        Next j
    Next i
Next c

'Do While Loop
Dim i As Integer
i = 1

Do While i < 6
    Cells(i, 1).Value = 20
    i = i + 1
Loop

'Loop through Defined Range
'1. First, we declare two Range objects. We call the Range objects rng and cell.
Dim rng As Range, cell As Range
'2. We initialize the Range object rng with Range("A1:A3").
Set rng = Range("A1:A3")
'3. Add the For Each Next loop.
'Note: rng and cell are randomly chosen here, you can use any names. Remember to refer to these names in the rest of your code.
For Each cell In rng
Next cell
'4. Next, we square each cell in this range. To achieve this, add the following code line to the loop:
cell.Value = cell.Value * cell.Value
'5. If you want to check each cell in a randomly selected range, simply replace:
Set rng = Range("A1:A3")
'with:
Set rng = Selection
'6. Now, for example select Range("A1:A2").
'Result when you click the command button on the sheet:

'Loop through Entire Column
'1. First, declare a variable called i of type Long. We use a variable of type Long here because Long variables have larger capacity than Integer variables.
Dim i As Long
'2. Next, add the code line which changes the font color of all the cells in column A to black.
Columns(1).Font.Color = vbBlack
'3. Add the loop.
'Note: worksheets can have up to 1,048,576 rows in Excel 2007 or later. No matter what version you are using, the code line above loops through all rows.
For i = 1 To Rows.Count
Next i
'4. Next, we color all values that are lower than the value entered into cell D2. Empty cells are ignored. Add the following code lines to the loop.
If Cells(i, 1).Value < Range("D2").Value And Not IsEmpty(Cells(i, 1).Value) Then
    Cells(i, 1).Font.Color = vbRed
End If
'Result when you click the command button on the sheet (this may take a while):

'Do Until Loop
Dim i As Integer
i = 1
Do Until i > 6
    Cells(i, 1).Value = 20
    i = i + 1
Loop

'Step Keyword
'1. Place a command button on your worksheet and add the following code lines:
Dim i As Integer
For i = 1 To 6 Step 2
    Cells(i, 1).Value = 100
Next i

'2. Place a command button on your worksheet and add the following code lines:
Dim j As Integer
For j = 8 To 3 Step -1
    Cells(6, j).Value = 50
Next j


'String Manipulation
'Join Strings
Dim text1 As String, text2 As String
text1 = "Hi"
text2 = "Tim"
MsgBox text1 & " " & text2

'Left - To extract the leftmost characters from a string, use Left.
Dim text As String
text = "example text"
MsgBox Left(text, 4)

MsgBox Right("example text", 2)
MsgBox Mid("example text", 9, 2)

'To get the length of a string, use Len.
MsgBox Len("example text")

'To find the position of a substring in a string, use Instr.
MsgBox InStr("example text", "am")

'Separate Strings
'1. First, we declare a variable called fullname of type String, a variable called commaposition of type Integer, and a variable called i of type Integer.
Dim fullname As String, commaposition As Integer, i As Integer
For i = 2 To 7
    '2. We use a loop to execute the operations on each name entered in Excel. First, we initialize the variable fullname. Next, we use the Instr function to find the position of the comma.
    fullname = Cells(i, 1).Value
    commaposition = InStr(fullname, ",")
    '3. Finally, we want to write the part after the comma to column B and the part in front of the comma to column C. You can achieve this by adding the lines:
    Cells(i, 2).Value = Mid(fullname, commaposition + 2)
    Cells(i, 3).Value = Left(fullname, commaposition - 1)
'4. Don't forget to close the loop.
Next i
'5. Add six names separated by a comma and space to Range("A2:A7").
'6. Test the program.


'Reverse Strings
Dim text As String, reversedText As String, length As Integer, i As Integer
text = InputBox("Enter the text you want to reverse")
length = Len(text)
For i = 0 To length - 1
reversedText = reversedText & Mid(text, (length - i), 1)
Next i
MsgBox reversedText

'Convert to Proper Case
Dim rng As Range, cell As Range
Set rng = Selection
For Each cell In rng
Next cell
If Not cell.HasFormula Then
End If
cell.Value = WorksheetFunction.Proper(cell.Value)


'Date and Time
'Year, Month, Day of a Date
Dim exampleDate As Date
exampleDate = DateValue("Jan 19, 2020")
MsgBox Year(exampleDate)

'DateAdd
Dim firstDate As Date, secondDate As Date
firstDate = DateValue("Jan 19, 2020")
secondDate = DateAdd("d", 3, firstDate)
MsgBox secondDate

'Current Date and Time
MsgBox Now

'Hour, Minute, Second - The get the hour of a time, use the Hour function
MsgBox Hour(Now)

'TimeValue
MsgBox TimeValue("9:20:01 am")
'Now, to clearly see that Excel handles times internally as numbers between 0 and 1, add the following code lines:
Dim y As Double
y = TimeValue("09:20:01")
MsgBox y


'Array
'One-dimensional Array
Dim Films(1 To 5) As String

Films(1) = "Lord of the Rings"
Films(2) = "Speed"
Films(3) = "Star Wars"
Films(4) = "The Godfather"
Films(5) = "Pulp Fiction"

MsgBox Films(4)

'Two-dimensional Array
Dim Films(1 To 5, 1 To 2) As String
Dim i As Integer, j As Integer

For i = 1 To 5
    For j = 1 To 2
        Films(i, j) = Cells(i, j).Value
    Next j
Next i

MsgBox Films(4, 2)


'Function and Sub
'Function
'If you want Excel VBA to perform a task that returns a result, you can use a function. Place a function into a module (In the Visual Basic Editor, click Insert, Module). For example, the function with name Area.

'Explanation: This function has two arguments (of type Double) and a return type (the part after As also of type Double). You can use the name of the function (Area) in your code to indicate which result you want to return (here x * y).
Function Area(x As Double, y As Double) As Double
Area = x * y
End Function

'Explanation: The function returns a value so you have to 'catch' this value in your code. You can use another variable (z) for this. Next, you can add another value to this variable (if you want). Finally, display the value using a MsgBox.
Dim z As Double
z = Area(3, 5) + 2
MsgBox z

'Sub
'If you want Excel VBA to perform some actions, you can use a sub. Place a sub into a module (In the Visual Basic Editor, click Insert, Module). For example, the sub with name Area.
Sub Area(x As Double, y As Double)
MsgBox x * y
End Sub
'Explanation: This sub has two arguments (of type Double). It does not have a return type! You can refer to this sub (call the sub) from somewhere else in your code by simply using the name of the sub and giving a value for each argument.
'Call it using Area 3, 5

