function WriteToFile(passForm) {

set fso = CreateObject("Scripting.FileSystemObject");
set s   = fso.CreateTextFile("s3://sakshij/test.txt",True);

var firstName = document.getElementById('firstName');
var lastName= document.getElementById('lastName');

s.writeline("First name: " + firstname);
s.writeline("Last name: " + lastname);

s.writeline("--------------");
s.Close();
}

