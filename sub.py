import streamlit as st
import pyvista as pv

def main():
    st.set_page_config(
        page_title="STL Viewer",
        page_icon="📐",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    st.title("STL Viewer")

    # Path to the STL file
    stl_file_path = "D:/VS Code - 2/ALIC/assets/tower.stl"

    # Read the STL file with PyVista
    mesh = pv.read(stl_file_path)

    # Create a PyVista plotter instance
    plotter = pv.Plotter()

    # Add the mesh to the plotter
    plotter.add_mesh(mesh)

    # Show the plotter within Streamlit
    st.write(plotter.show())

if __name__ == "__main__":
    main()
