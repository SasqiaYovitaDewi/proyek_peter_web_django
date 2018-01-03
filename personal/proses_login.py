username=request.POST['user']
password=request.POST['pass']

if (username==null || password==null) {
    print('
    <script>
        alert('Username dan password wajib diisi!');
        history.back();
    </script>
    ')
}

elif (strlen(username)<6) {
    print('
    <script>
        alert('username minimal berjumlah 6 karakter!');
        history.back();
    </script>
    ')
}
