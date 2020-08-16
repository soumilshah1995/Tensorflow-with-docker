
# from dotenv import load_dotenv
# load_dotenv()

try:
    from API import (app,
                     api,
                     Embeddings)
except Exception as e:
    print("Modules are Missing : {} ".format(e))


api.add_resource(Embeddings, '/embedding')

if __name__ == '__main__':
    app.run(debug='0.0.0.0')
