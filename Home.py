import streamlit as st

# Titre 
st.title("Hello World !")

# Sous-titre
st.subheader('This is a subheader')

# Texte
st.write("This is a simple text.")

# Champs de saisie
user_input = st.text_input('Tape your text')

# Afficher à l'écran ce que l'utilisateur a saisi
st.write(user_input)

# Ajputer une image
st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWkAAACMCAMAAACJW6j5AAABGlBMVEX///8aG0H/twBITOXmQ64VFj8YGUAAADUsLUzm5uoAADLZ2d4XGUIAADOkpLD5+fsAACo9PVkAADft7fAAAC0PEDudnau2t7/AwMZbW3OBgZESEz0ICzkNDzsAACkGCDnKytEmJ0vU1NqSkqBSU2tkZHhsbIDlNao+Q+Srq7ZiYnhMTGaKipl4eIo4OVdERWA2O+P/ugAAACQtLkz63vCChOz/+elyder/8tbd3fr//PQhIkoAABjzq9jsfcTqa7zxoNOZnO96fetqbem0tfPm5vv/57z/0G//xlj/wUDpXrj40OnFxvZeYej/2pHvj8svNOP/vir+8vr/4KX1vuDP0fiPke1UV+f85/WwsfP/25n0tt3t7f3/0nucBfg5AAAPqUlEQVR4nO1dW2PaxhKG2FohYSGQBAIkWQIENnfHTpq2Ps2lJye33pumSdvk//+NgxLbQdqZ1S6IgKm+B7+w1o4+7c7OzM7OFgo5NgDTnrTm89a00t22JPuNoFXVfIcQx5OtTkXftjh7C6WlesUbSOpFsG2J9hRdzy3G4KiVbcu0lwg0qZgAsXKqs4fiUUQvqFaDbcu1fxj5NNELBTLLl8WM0bQgootFdbhtyfYNcwdmWupsW7I9g3IME10sVnMXJlNUNIxpOTc/MsXAxZiuD7Yt235hBph4V4q6tm3Z9guXKNPFfEnMFB2CMl3ctmz7hTFi5C3cxNK2Zdsv4CuiE25btv1CRcaYlnvblm2/gHsuVrBt2fYMmKKWLrct2b4hwCJMjW1LtndowVHTUh41zRrKEeS8WM1ty7WHCCxgdys3PDaBplFPrIbWZNsy7SnKNXVpWBO5mO+3bAr6sKh6ThQCkXzVmJjblmefodujuVM9P+5M7dzoyJEjR44cOXLkyJEjR44cOXLkyJEjx27D7DbtoW0HSno4Uy/bw0qjUanY5S8V+9TN7rDXHvTD+TwcDdq9YaBsKLxtlpuVRU+tcW3e6k/bPbtsZveSpt3rXx5bqqqpqlq1Su0hTrdSmZYsS9XkBTTVkueT5qYj+nq50S/Jlib7rld3HMdzfUOztE6/1824a8Vuh0dVVTMWPS06qi96klXLmA2GWQwpxe57qrx8hk3yVbU2KUNtG2NV82M7r45heX17c2Sbdr+kacAROyJ5stppZde1Uhl7qu8AWbGSqxmzaXM9srv9I9WjH04k2R8FybYDV4MEIZ56OVHWEgND0Dc0V8JTgiVPM1qZZDIEoQy+3Ge2VWkKjT4+dMeqiz19wd94+cnmSPVRSSRDa7M/uW6DYI7IYF5FxVuS05qty7U+LFn1tI6KxD/vr8a1MjiuM1+kXp3eMNGw2C9NDJm51a1EawCFc4bkQWihWddxONZ8Ha714aWKn1mIwbUGK3BtG2ACV4w+2bM/tlVaaqoUxAoZKkQ5gvSOjMrdHXGMshs4VhiIM/AJzRovz5HEvjwQXBn0qZo6MYtR9kuUZhQ4aKb5MtwjG+1PkOmJzNXjZ3haW4yAK5h9jXPmXEOWhPJU9FDjIXpBhtYq2HQZAxgSnv4lxLRS45RuGfLFChM7wBcqxlv2+c0QfYYm6VNwJXwlpGBhI0uE6aYmoDg+w6niUwrBpCr+RRcwSrwfVSmJzE0iIg1GtQDTPS69BgkqmOhnhqv25Mh8H9UseekPWxUq/Lb8TA/SF18MRBWY1wWlk2oSMHriSrGHs8azggXKwM10Cz1izgOZ/yiY4q2ko65FVzkykierDxougIeEeJkO+RcQEMacl2hf0OZIyl5NVVXN8/XeJRWSC1icnEz31xrREeQWF9FmZz2iF6imKBAdCHNkDB+ob8DH9HRtootFjae6gj4XtNcBEIttWLfXnJ48Iqi0c8zFdCMTvcajQftZsEDkgNFF2dj4kI4KWa3EdFDNpHeSfk6pgRzaE4REGJ55a/1ZwwG6kBUH06bMHgREcjzPdT2PFd382FBLCU2U0+aOFO0CRPsOKT25uKnTzeZjpkE6WoHpPsv4jLYnOvNWfzDoj8YXsiqzFjQ3ZVUcs/wJx7CMi/Eo6qk176iaywpF4LUVp+jbEMeXZcPnjHDUo90txtpqJX2odKZthsPmWqWprdxs6JmK3a5VGR9GZbpwPXzdJYY1njRvNvd0szycdiz8w6DTB52gRLbG7V6l165Z6WuFpBmtSaMxaXkqZvzXk9MqlWm9hH5ktzoI6HcpTy10zZE6DF9RQf+NaAaweaQ3w2OUa3cEd4LV+JLlxvW3UdrnbF+daJ3KVWPdDunznFdPTEicyjRqEznqAIl7m20NE1VmxFBHyFJFfKOBfKByC4thQ3ZWBGTcqNPlHswRa8FIREabSOhaSyiwNKYVbEZrc0ZFPSXERNXQaBtm4RCNFeNvlhBl5YBOqQ67h1R14gauQSQviLc1xwbULqk+0pgeIC+iTfG3jzBBItmQ9/QJM3gtlQy2H6JjARlwTWiCIwBYP1EXghjUCNNDaFSTy/gASWFaQQLFSGRwCRVEVAtROUj9C46ywQOYanBQT6CxakCjpo/oMg3w9c0OpJPU+CdJYRrR0jwBZ8QLwTR1CKv28yC9pxEiJPCvUIFAIkHayTwGxxislGxoWCUUNZtpHTYH0lTHJyCxySq4unXhgUlZpSDG4PirA9Y7VLZOhiNSE1D7IlMM+oJ+nCU207BNVOeMgMJ+rwbq3Sk4LjW+zRod3nQ8phSVCWQDkTqsz8rQnMSqJg0Borz4l2YzDZZpIj7nbp0JPRuef7DVzvtJkTLadH20MjBOnTH8TB0apwby6RXAcHLmsdnLZBoSbDHQuOusDEH9YQAfCrYJtIC3J9AWp4toB8DQQ018yG9HrPRCAVCz0gU/0z1oSksCNZrAQuKQXgRLJLr89YJBs59oSYMMWrmSHsYNIEWNWU6QoiZHsZWWyXQIEYVKBgBck4HykjoohSqQKALa/ZT6gORBhynkvVQxJ6pFxz9InZtpBRrSxBHIygLVL/GpgQEa01SMhoUuFDmiloRdZRockT6XhXcNUP/Q79aDFgSxAmfQ4k2OEt90V5luQzPSErpAoAyFXOk1qAbR5It0BNpZlPW7q0yD728IvX8B8lNpRW0BQvhiqZOgnZQ0ynaUaR1UHoKpo9ACTryE9QLuOLF3DWhA5q/Xj7fZUaZBJwn28HCAhnI1YVSAM98SzIeGdJ2UuGtpR5m2wfcXPTjDM1xhkgQ7CqBvasSZ2VGmwWi4dHFREsHFEfCQpO8SAptxpCjWUakEuf5WfPbsKNNTMI4pCQJ6RlLZgxdDEMGOwCBTYvbsKNMh/zETQSTjmSkJJWsgMXt2lOnZxt4/oYPNzSXKJcy8HWWaddnLeiDxKG95g2P6VjC9wUTBuPtTXuGcEifceOxgR5nO4EUxHMekRHa2skDCdfkXMh1zKKD4fEZIbKj8+5iuxvyfDTKduBJvR5m+zOBNEcQF3uSYjkeod5TpztrviSKuPTaop2+H9gDd22yQZHpjPSV8pB1lurYxH7FYjUmpbM6evh22R2vt82oYEtsJG/QR/VthT2cTYYLgJBIx4Jy0LHq6HT5iA8yrEYyawkhsb4Gpmp0sOurciggTuBMiuI3IB0DMoreJa7h3lGlwE0Nsa5wT0GYj80jMqthRpk3oQlCRDCZuwPuIGyhAt6NMF6BtDCwzcy2Ae+PyBr7prjINqc/i+SZKpkKHiTbxTXeVaTCHSzQNgwtQroZwGgIHdpVpMC8RPuixJsCTDsipiHVgn2sUzlGmgcb/wZgOLbqxxs20CR6Ex6sWrg4wp38D90OXGxUKDWzl7dJtK9gR1IINNK7wZ6qPIC9RIH+cG/DJJbpyw20Gk2nQ+irKGzCpwTMBIqcPdh9MphWwkq3HnUGuI6BbgqnaAidq+HvaGthnt0A7j3tWT2Y1CDPg/JN5CaYx8Z4Sm4Md1UoB379/EbCZhoca5wEU89gBA3lgNTm4wEm9BjSlYVtwyNC4PWO6AJfhkXweUxepIkGfXYuA7LsYPLXfdALvWWxi7V4dKUyD51QWqrqWTjV8GBE9/wceqIsKb6S/wwDZSQAnz9aQwrSJ0OXP0+I/AVaB5hhWPfAxWZ4z6ljtTLro1FaRVt8DGdRF9zJgPjfAKkehPiZS36Moj9kfFS0hDNWH2CLSmNaxgmmSNWWsNw208jx69g2tyucZrKjeACOacC0mXw6pdZiwiihFYvhDhGulhRalc3BrAi0ZSNRagPxPswNuwUXgN8a/DNKruCFL1UcGSj1gZpenBl5mEY2cMVNOHSsc0iNUb7awwl5R1GS3hjQH06xcLkk2wl53iW2l2xsz7pdJ1ryIY8Loqa6S/nDplim93GzPWNdwsLT0ve8ePnr08PE9LobePPn+vw/uP/0fT9tvnz1/8fLF82dfAb9x1ICEi5xcw5HVo4taOBoMRuH8gqgysxImVZ1gGfoFK8OEeJrcmc1bi55aYa3kqsxqjYyYyb1HJycnh4eHJyevfkjl7sefzk5PDw5OT0/vp3P98907V/jwLfUjTwXZUkqKDbkpN8q4IOoT0ewaNODZ5+WOrnpadJTSE6min/S7iOUrnPySwt33ZwfXOP31R3bbr254jvB18mceppWs8uaAWsFxVLIq74rfIvPPEtGpVD84PVjCGZPqONF37iQ1CFf9aVZpUwEQNXW7G6nIJgoPtXB+iBG9oPofhjRPzg5iOP2G0fhlnOg7vyUUCF9N9WyuMOC41yWLmupAtYnPOEzi5HdUmG9ODxJMP8Alf30niZ9XYTqDewIYt/csw+ysf9MKo6T4HycU07j+uJ9k+uDsDdr4LsV0Qn/w3n2xxm0uV+ArslcwhW4PAsGInz+ixvThIdb2fZLnxaD+E2v8jCb6zrOVmF6bag0pU0zBnK13rQ3Bq3wXdIDoE8ysfnNGU/0We/LPANPPYy347yhqr7UsWvxFhfT5OvnUEmtH6B3ENGZUP6WUx0J9YE9+DjD9ItZC4N6tCVRZhg8c19ksQe+v3pMjs6o33aPUNIPpvwCmf8X8oRcA0y9jLUTukrNFLqGMvb4mmPg0weMZbBglpiEpNKZ/BLTHKfbkD1mO6RXvR1yo6Jlw2mjQWUWDSKk3qUFMv0PafgMw/RP24L8Bpj/EyRO787OXfvVrEh5nGdg49KnonZ/FotxJnToPafXxChXhLT2kn2CNv87O9rhCeVAVUiGO1VoxEac5E1uCXbWdHidNuoiLIf0d2vgJbU/jTuJvFNF3406iKNPRFd3HvFwTx5oFqW+PYmhw3xlM3PM+l4p6RTGNt31P+Yj38ca0Qf13vIE40wuuWxrHCUIiGep4zRvHKx2e+2yJoxlTzqXgXTLuwQqcPk1o6rfvGY2Tdt7LxO+rMB1tq1yqzDuCinVZm7UzSOALBpcq85Y94mn+vMK/5Mb98ZPHzMZ/xqhmBpgK38ZDTHeTEerVmF54cva0ZCG3ITmGGm3FpL40H0y7X0R6Ip5sFfsVsTTjHw5vuD5hRvIi/HV2o0FO3zKJXlC9bFO/oLZdVmW6EG0wNfqXx6omu1FWGJEkxzNkzarK40kz2z08M+h97MmI9gCimmOOa2iqdez1G13xnt798nHPZfHnYfr+1psHv55GODt9wlIdn/D6elm8+5r+UTF8l4JvcQ8TMxhW2qNwXKvNw9a0N7SDTW2ULnpqLHqa12rjcDRtDO3uyll3v//x+OHDx3/g8dJlvH/65P6ff73h6+zr1x9efPib2m+JYLYhROvL/wG59JSCrP0j9AAAAABJRU5ErkJggg==')

# Création d'un formulaire
with st.form('Form1'):

    # On demande à l'utilisateur son nom
    user_name = st.text_input('Tape your name : ')

    # Bouton "Envoyer"
    if st.form_submit_button("Send"):
        # On affiche le nome de l'utilisateur
        st.write(user_name)