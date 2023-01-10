import streamlit as st

st.image('src/images/neuron.jpg')

st.title('¡Hola Neurona!')

tab1, tab2, tab3 = st.tabs(['Una entrada', 'Dos entradas', 'Tres entradas y sesgo'])

with tab1:
    st.markdown('Peso $w_0$')
    peso = st.slider('', 0.0, 5.0)
    input_data = st.number_input('Introduzca el valor de la entrada')

    calculate = input_data * peso

    if st.button('Calcular la salida', key='button_1'):
        st.write(calculate)

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('Peso $w_0$')
        peso_1 = st.slider('', 0.0, 5.0, key='peso_1')

        st.markdown('Entrada $x_0$')
        input_data_1 = st.number_input('', key='input_data_1')

    with col2:
        st.markdown('Peso $w_1$')
        peso_2 = st.slider('', 0.0, 5.0, key='peso_2')

        st.markdown('Entrada $x_1$')
        input_data_2 = st.number_input('', key='input_data_2')

    
    calculate = input_data_1 * peso_1 + input_data_2 * peso_2

    if st.button('Calcular la salida', key='button_2'):
        st.write(calculate)

with tab3:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('Peso $w_0$')
        peso_1 = st.slider('', 0.0, 5.0, key='peso_3')

        st.markdown('Entrada $x_0$')
        input_data_1 = st.number_input('', key='input_data_3')

    with col2:
        st.markdown('Peso $w_1$')
        peso_2 = st.slider('', 0.0, 5.0, key='peso_4')

        st.markdown('Entrada $x_1$')
        input_data_2 = st.number_input('', key='input_data_4')

    with col3:
        st.markdown('Peso $w_2$')
        peso_3 = st.slider('', 0.0, 5.0, key='peso_6')

        st.markdown('Entrada $x_2$')
        input_data_3 = st.number_input('', key='input_data_6')

    sesgo = st.number_input('Introduzca el valor del sesgo')

    

    calculate = input_data_1 * peso_1 + input_data_2 * peso_2 + input_data_3 * peso_3 + sesgo

    if st.button('Calcular la salida', key='button_3'):
        st.write('La salida de la neurona es', calculate)
