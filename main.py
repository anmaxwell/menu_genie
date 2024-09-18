import mesop as me

@me.stateclass
class State:
  is_open: bool = False

@me.page(path="/")
def page():
  with me.box(
    style=me.Style(
      background="#fff",
      min_height="calc(100% - 48px)",
    )
  ):
    with me.box(
      style=me.Style(
        width="min(720px, 100%)",
        margin=me.Margin.symmetric(horizontal=75, vertical=36),
      )
    ):
      header()
      test_layout()
      apikey_input()
  footer()

def header():
  with me.box(
    style=me.Style(
      padding=me.Padding(
        top=24,
        bottom=36,
      ),
    )
  ):
    me.text(
      "Meal Genie",
      style=me.Style(
        font_size=36,
        font_weight=700,
        background="linear-gradient(90deg, #4285F4, #AA5CDB, #DB4437) text",
        color="transparent",
      ),
    )

def test_layout():
  state = me.state(State)

  with dialog(state.is_open):
    me.text("Delete File", type="headline-5")
    with me.box():
      me.text(text="Would you like to delete cat.jpeg?")
      me.button("No", on_click=on_click_close_dialog)
      


  with me.box(style=me.Style(padding=me.Padding.all(30))):
    me.button(
      "Open Dialog", type="flat", color="primary", on_click=on_click_open_dialog
    )

def apikey_input():
  with me.box(
     style=me.Style(
        display="flex",
        flex_direction="row",
        justify_content="right")
    ):
     me.button("API Key", type="stroked")

def footer():
  with me.box(
    style=me.Style(
      position="sticky",
      bottom=0,
      padding=me.Padding.symmetric(vertical=16, horizontal=16),
      width="100%",
      background="#F0F4F9",
      font_size=14,
    )
  ):
    me.html(
      "Made with <a href='https://google.github.io/mesop/'>Mesop</a>",
    )

def on_click_close_dialog(e: me.ClickEvent):
  state = me.state(State)
  state.is_open = False


def on_click_open_dialog(e: me.ClickEvent):
  state = me.state(State)
  state.is_open = True


@me.content_component
def dialog(is_open: bool):
  """Renders a dialog component.

  The design of the dialog borrows from the Angular component dialog. So basically
  rounded corners and some box shadow.

  One current drawback is that it's not possible to close the dialog
  by clicking on the overlay background. This is due to
  https://github.com/google/mesop/issues/268.

  Args:
    is_open: Whether the dialog is visible or not.
  """
  with me.box(
    style=me.Style(
      background="rgba(0, 0, 0, 0.4)"
      if me.theme_brightness() == "light"
      else "rgba(255, 255, 255, 0.4)",
      display="block" if is_open else "none",
      height="100%",
      overflow_x="auto",
      overflow_y="auto",
      position="fixed",
      width="100%",
      z_index=1000,
    )
  ):
    with me.box(
      style=me.Style(
        place_items="center",
        display="grid",
        height="100vh",
      )
    ):
      with me.box(
        style=me.Style(
          background=me.theme_var("surface-container-lowest"),
          border_radius=20,
          box_sizing="content-box",
          box_shadow=(
            "0 3px 1px -2px #0003, 0 2px 2px #00000024, 0 1px 5px #0000001f"
          ),
          margin=me.Margin.symmetric(vertical="0", horizontal="auto"),
          padding=me.Padding.all(20),
        )
      ):
        me.slot()
