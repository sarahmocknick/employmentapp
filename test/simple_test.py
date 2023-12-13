# test for simple job searching 

from app.simple import simple_job_search

def test_simple_job_search():
    data = simple_job_search()
    assert data is not None
    assert len(data) > 2

    # Check if the 'results' key exists in the returned data
    assert 'results' in data

    # Check if 'results' is a list
    if 'results' in data:
        assert isinstance(data['results'], list)
        assert len(data['results']) > 0

        # Check the structure of the first item in the 'results' list - used ChatGPT for line 22
        first_result = data['results'][0]
        assert isinstance(first_result, dict)
        assert all(key in first_result for key in ['title', 'company', 'location', 'description'])
   