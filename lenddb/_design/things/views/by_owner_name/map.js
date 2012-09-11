function(doc)
{
    if(doc.doc_type == "Thing")
    {
        emit([doc.owner, doc.name], null);
    }
}
