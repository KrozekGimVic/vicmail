% rebase('base.tpl', title='Pozdrav')

<h1>Greeter</h1>

% if hello_msg:
<h2>
Pozdravljeni, {{hello_msg}}!
</h2>
% else:
<form action="/greet/" method="get">
  Ime: <input type="text" name="fname" value={{firstname}}><br>
  Priimek: <input type="text" name="lname" value={{lastname}}><br>
  <input type="submit" value="Submit">
</form>
% end

Za krajo identite ne odgovarjamo.