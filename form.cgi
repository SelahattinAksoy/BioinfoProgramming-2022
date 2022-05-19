#!/usr/bin/env python3
import cgi;
import cgitb;cgitb.enable()

print("Content-Type: text/html")
print()

print('''

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

''')

print('''

<div class="container">
  <h1 class="text-center m-1"><em>Selahattin AKSOY</em></h1><hr>
  <div class="row">
    <div class="col-sm">
    </div>
    <div class="col-sm mt-1  text-center text-white bg-info rounded ">


<form action="selo2.cgi"  class="p-3">
  <div class="form-group mt-1">
    <label for="exampleInputEmail1">ID</label>
    <input type="text" name="id"  class="form-control" placeholder="Enter email" required>
  </div>

  <div class="form-group">
    <label for="exampleInputPassword1">Type</label>
   <input type="text" name="type" class="form-control"  placeholder="Enter type" required>

  </div>

<div class="form-group">
    <label for="exampleInputPassword1">DB</label>
    <input type="text" name="db" class="form-control"  placeholder="Enter Database" required>

  </div>


  <button type="submit" class="btn btn-success">Search</button>
</form>


    </div>
    <div class="col-sm">
    </div>
  </div>
</div>


''')
