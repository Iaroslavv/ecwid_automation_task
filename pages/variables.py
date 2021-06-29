import pytest

search_parameters = [
        pytest.param("drss", marks=pytest.mark.xfail(reason="there aren't any items with missing letter")),                                                                            
        pytest.param("dressg", marks=pytest.mark.xfail(reason="there aren't any items with extra letter")),                                                                       
        pytest.param("black.dress", marks=pytest.mark.xfail(reason="there aren't anyany items with symbol inside")),                                                                             
        "dress#",
        "%&dress",
        pytest.param("hdress", marks=pytest.mark.xfail(reason="there aren't any items with a letter before an item")),                                                                          
        "dress shorts surf woven",
        "dresses",
        "shirt", 
    ]
