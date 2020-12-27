
Sub destinos()

Dim i As Integer
Dim rows As Integer
Dim states(15), destination(15) As String
Dim final As String

Range("B7").Select
rows = Range(Selection, Selection.End(xlDown)).Count
For i = 0 To rows - 1
states(i) = Range("B7").Offset(i, 0)
destination(i) = Range("B7").Offset(i, 1)
Next

final = """cities""=> {""countries""=>[""Chile""], ""states""=>["
For i = 0 To rows - 1
If i <> rows - 1 Then
final = final & """" & states(i) & ""","
Else
final = final & """" & states(i) & """],""destinations""=> ["
End If
Next

For i = 0 To rows - 1
If i <> rows - 1 Then
final = final & """" & destination(i) & ""","
Else
final = final & """" & destination(i) & """]}"
End If
Next

Sheets("Final").Range("A1").Value = final

End Sub

'#################################################################################################

Sub branches()

Dim rows, columns As Integer
Dim valu(100, 16) As String
Dim final As String

columns = 16
rows = 0
For p = 0 To 100
If Sheets("Sucursales|Branches").Cells(4 + p, 1) <> "" Then rows = rows + 1
Next p

For i = 0 To rows - 1
For j = 0 To columns - 1
valu(i, j) = Sheets("Sucursales|Branches").Range("A4").Offset(i, j)
Next j
Next i

final = """branches""=> "

For i = 0 To rows - 1
For j = 0 To columns - 1
Select Case j
Case Is = 0
    final = final & " {""name""=>" & """" & valu(i, j) & ""","
Case Is = 1
    final = final & """work_number""=>" & """" & valu(i, j) & ""","
Case Is = 2
    final = final & """additional_phone_numbers""=>" & """" & valu(i, j) & ""","
Case Is = 3
    final = final & """fax_number""=>" & """" & valu(i, j) & ""","
Case Is = 4
    final = final & """email""=>" & """" & valu(i, j) & ""","
Case Is = 5
    final = final & """business_status""=>" & """" & valu(i, j) & ""","
Case Is = 6
    final = final & """address_line1""=>" & """" & valu(i, j) & ""","
Case Is = 7
    final = final & """address_line2""=>" & """" & valu(i, j) & ""","
Case Is = 8
    final = final & """city""=>" & """" & valu(i, j) & ""","
Case Is = 9
    final = final & """state""=>" & """" & valu(i, j) & ""","
Case Is = 10
    final = final & """pin_code""=>" & """" & valu(i, j) & ""","
Case Is = 11
    final = final & """country""=>" & """" & valu(i, j) & ""","
Case Is = 12
    final = final & """allow_cancellation""=>" & """" & valu(i, j) & ""","
Case Is = 13
    final = final & """discount""=>" & """" & valu(i, j) & ""","
Case Is = 14
    final = final & """date_type""=>" & """" & valu(i, j) & ""","
Case Is = 15
    If i <> rows - 1 Then
    final = final & """collection_day""=>" & """" & valu(i, j) & """}, "
    Else
    final = final & """collection_day""=>" & """" & valu(i, j) & """} "
    End If
End Select
Next j
Next i

Sheets("Final").Range("A2").Value = final

End Sub

'#################################################################################################

Sub users()

Dim rows, columns As Integer
Dim valu(100, 21) As String
Dim final As String

columns = 21
rows = 0
For p = 0 To 100
If Sheets("Usuarios|Users").Cells(4 + p, 1) <> "" Then rows = rows + 1
Next p

For i = 0 To rows - 1
For j = 0 To columns - 1
valu(i, j) = Sheets("Usuarios|Users").Range("A4").Offset(i, j)
Next j
Next i

final = """users""=> "

For i = 0 To rows - 1
For j = 0 To columns - 1
Select Case j
Case Is = 0
    final = final & " {""login""=>" & """" & valu(i, j) & ""","
Case Is = 1
    final = final & """email""=>" & """" & valu(i, j) & ""","
Case Is = 2
    final = final & """first_name""=>" & """" & valu(i, j) & ""","
Case Is = 3
    final = final & """last_name""=>" & """" & valu(i, j) & ""","
Case Is = 4
    final = final & """sex""=>" & """" & valu(i, j) & ""","
Case Is = 5
    final = final & """travel_branch_id""=>" & """" & valu(i, j) & ""","
Case Is = 6
    final = final & """home_number""=>" & """" & valu(i, j) & ""","
Case Is = 7
    final = final & """mobile_number""=>" & """" & valu(i, j) & ""","
Case Is = 8
    final = final & """work_number""=>" & """" & valu(i, j) & ""","
Case Is = 9
    final = final & """fax_number""=>" & """" & valu(i, j) & ""","
Case Is = 10
    final = final & """other_numbers""=>" & """" & valu(i, j) & ""","
Case Is = 11
    final = final & """city""=>" & """" & valu(i, j) & ""","
Case Is = 12
    final = final & """state""=>" & """" & valu(i, j) & ""","
Case Is = 13
    final = final & """zip_code""=>" & """" & valu(i, j) & ""","
Case Is = 14
    final = final & """address_line1""=>" & """" & valu(i, j) & ""","
Case Is = 15
    final = final & """address_line2""=>" & """" & valu(i, j) & ""","
Case Is = 16
    final = final & """country""=>" & """" & valu(i, j) & ""","
Case Is = 17
    final = final & """title""=>" & """" & valu(i, j) & ""","
Case Is = 18
    final = final & """cc_mail_ids""=>" & """" & valu(i, j) & ""","
Case Is = 19
    final = final & """role_id""=>" & """" & valu(i, j) & ""","
Case Is = 20
    If i <> rows - 1 Then
    final = final & """tieup_operator""=>" & """" & valu(i, j) & """}, "
    Else
    final = final & """tieup_operator""=>" & """" & valu(i, j) & """} "
    End If
End Select
Next j
Next i

Sheets("Final").Range("A3").Value = final

End Sub

'#################################################################################################

Sub stations_stages()

Dim rows, columns As Integer
Dim valu(100, 19) As String
Dim final As String

columns = 19
rows = 0
For p = 0 To 100
If Sheets("Terminales|Stations").Cells(5 + p, 1) <> "" Then rows = rows + 1
Next p

For i = 0 To rows - 1
For j = 0 To columns - 1
valu(i, j) = Sheets("Terminales|Stations").Range("A5").Offset(i, j)

Sheets("Final").Range("A14").Value = Sheets("Final").Range("A14").Value & " | " & Sheets("Terminales|Stations").Range("A5").Offset(i, j)
Next j
Next i

Dim rows2, columns2 As Integer
Dim valu2(100, 4) As String

columns2 = 4
rows2 = 0
For p2 = 0 To 100
If Sheets("Etapas|Stages").Cells(4 + p2, 1) <> "" Then rows2 = rows2 + 1
Next p2

For i2 = 0 To rows2 - 1
For j2 = 0 To columns2 - 1
valu2(i2, j2) = Sheets("Etapas|Stages").Range("A4").Offset(i2, j2)

Sheets("Final").Range("A15").Value = Sheets("Final").Range("A15").Value & " | " & Sheets("Etapas|Stages").Range("A4").Offset(i2, j2)

Next j2
Next i2

Dim z As Integer

final = """stages_format""=> "

For i2 = 0 To rows2 - 1

z = 0
For i = 0 To rows - 1
If valu2(i2, 1) = valu(i, 0) Then z = i
Next i

    final = final & " {""name""=>" & """" & valu(z, 0) & ""","

    final = final & """stage_type""=>" & "-" & ","

    final = final & """route_id""=>" & """" & valu2(i2, 0) & ""","

    final = final & """contact_numbers""=>" & """" & valu(z, 2) & ""","

    final = final & """contact_persons""=>" & """" & valu(z, 3) & ""","

    final = final & """city""=>" & """" & valu(z, 1) & ""","

    final = final & """state""=>" & "-" & ","

    final = final & """pin_code""=>" & """" & valu(z, 10) & ""","

    final = final & """landmark""=>" & """" & valu(z, 11) & ""","

    final = final & """comments""=>" & """" & valu(z, 14) & ""","

    final = final & """address_line1""=>" & """" & valu(z, 5) & ""","

    final = final & """address_line2""=>" & """" & valu(z, 15) & ""","

    final = final & """time""=>" & """" & CStr(valu2(i2, 2)) & ""","

    final = final & """country""=>" & """Chile""" & ","

    final = final & """is_next_day""=>" & "-" & ","

    final = final & """default_stage""=>" & """" & valu(z, 16) & ""","

    Select Case valu2(i2, 3)
    Case Is = "Embarque"
        final = final & """is_pick_up""=>" & """" & "0" & ""","
    Case Is = "Bajada"
        final = final & """is_pick_up""=>" & """" & "1" & ""","
    Case Else
        final = final & """is_pick_up""=>" & """" & "-" & ""","
    End Select
    
    final = final & """is_eticketing""=>" & """" & valu(z, 17) & ""","

    If i <> rows - 1 Then
    final = final & """is_api""=>" & """" & valu(z, 18) & """}, "
    Else
    final = final & """is_api""=>" & """" & valu(z, 18) & """} "
    End If

Next i2

Sheets("Final").Range("A12").Value = final

End Sub

'#################################################################################################

Sub a()

For j2 = 0 To 18 'columns2 - 1

Select Case j2
Case Is = 0
    final = final & " {""name""=>" & """" & valu(z, 1) & ""","
Case Is = 1
    final = final & """stage_type""=>" & "-" & ","
Case Is = 2
    final = final & """route_id""=>" & """" & valu2(i2, j) & ""","
Case Is = 3
    final = final & """contact_numbers""=>" & """" & valu(z, 3) & ""","
Case Is = 4
    final = final & """contact_persons""=>" & """" & valu(z, 4) & ""","
Case Is = 5
    final = final & """city""=>" & """" & valu(z, 2) & ""","
Case Is = 6
    final = final & """state""=>" & "-" & ","
Case Is = 7
    final = final & """pin_code""=>" & """" & valu(z, 7) & ""","
Case Is = 8
    final = final & """landmark""=>" & """" & valu(z, 8) & ""","
Case Is = 9
    final = final & """comments""=>" & """" & valu(z, 9) & ""","
Case Is = 10
    final = final & """address_line1""=>" & """" & valu(z, 5) & ""","
Case Is = 11
    final = final & """address_line2""=>" & """" & valu(z, 6) & ""","
Case Is = 12
    final = final & """time""=>" & """" & valu2(i2, j) & ""","
Case Is = 13
    final = final & """country""=>" & """Chile""" & ","
Case Is = 14
    final = final & """is_next_day""=>" & "-" & ","
Case Is = 15
    final = final & """default_stage""=>" & """" & valu(z, 11) & ""","
Case Is = 16
    final = final & """is_pick_up""=>" & """" & valu2(i2, j) & ""","
Case Is = 17
    final = final & """is_eticketing""=>" & """" & valu(z, 12) & ""","
Case Is = 18
    If i <> rows - 1 Then
    final = final & """is_api""=>" & """" & valu(z, 13) & """}, "
    Else
    final = final & """is_api""=>" & """" & valu(z, 13) & """} "
    End If
End Select
Next j2
Next i2

End Sub
