mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"tbartholomew@uvu.edu\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

web: sh setup.sh && streamlit run app.py