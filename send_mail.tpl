% rebase('base.tpl', title='Poslji')

<h1>Posiljaj posto</h1>

<form action="/send/" method="post">
  Email: <br><input type="text" name="email" value="{{to}}"><br>
  Naslov: <br><input type="text" name="naslov" value="{{subject}}"><br>
  Sporocilo: <br><textarea name="sporocilo" rows="20" cols="100">{{message}}</textarea><br>
  % end
  <input type="submit" value="Submit">
</form>