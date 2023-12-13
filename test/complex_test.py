# test complex_job_search.py

from app.complex import complex_job_search


def test_complex_job_search():
    data = complex_job_search()
    assert isinstance(data, dict)
    assert len(data) > 2

    # Check if the 'results' key exists in the returned data
    assert 'results' in data

    # Check if 'results' is a non-empty list
    if 'results' in data:
        assert isinstance(data['results'], list)
        assert len(data['results']) > 0

        # Check the structure of the first item in the 'results' list - used ChatGPT for line 21
        first_result = data['results'][0]
        assert isinstance(first_result, dict)
        assert all(key in first_result for key in ['title', 'company', 'location', 'salary_min', 'contract_time', 'description'])