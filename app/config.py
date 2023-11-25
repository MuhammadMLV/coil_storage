from fastapi import FastAPI

app = FastAPI(title='Warehouse App')


@app.get('/')
def initial_page():
    return 'Initial page'


@app.post('/api/coil')
def create_coil():
    pass


@app.delete('/api/coil')
def delete_coil():
    pass


@app.get('/api/coil')
def get_coil_list():
    pass
