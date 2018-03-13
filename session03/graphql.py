import graphene

def Query(graphene.ObjectType):
    hello = graphene.String() 

    def resolve_hello(self, args, context, info): 
        return 'Hello Aeon'
        
        schema = graphene.Schema(query=Query)
        result = schema.execute('{ hello }') 
        print(result.data['hello']) 


        
