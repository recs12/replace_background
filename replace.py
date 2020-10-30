import clr
import System
from System.IO.Path import Combine

clr.AddReference("System")


template_path = r"J:\PTCR\_Solidedge\Template"
PART = "Draft (part) TC.dft"
ASSEMBLY = "Draft (assembly).dft"


def combine(path1, path2):
    return Combine(path1, path2)


def get_category(model_links):
    # Get the type of draft part/plates or assembly?
    if model_links is None:
        return None
    else:
        category = model_links[0][-4:]
        return category


def replace_background(doc, template_path):
    for sheet in doc.Sheets:
        if sheet.Name == "Background FORMAT B":
            sheet.ReplaceBackground(template_path, "Background FORMAT B")
    print("[+] Background replaced\n")


def background(doc):
    """
    replace background in one draft.
    """
    if doc.Name.lower().endswith(".dft"):
                    print("Document name: %s" % doc.Name)
                    try:
                        if doc.ModelLinks.Count != 0:
                            # check if there is drawings on the draft.
                            model_links = [
                                link.FileName for link in doc.ModelLinks]
                            assert (
                                len(model_links) == 1
                            ), "This doc has different model links."
                            item_type = get_category(model_links).lower()
                            print("CAD type: %s" % item_type)
                        elif doc.ModelLinks.Count == 0:
                            # if there is not drawings inserted then
                            # we cannot identify the background to insert.
                            # so the app skip it.
                            item_type = ".pneu"
                            pass

                    except AssertionError as err:
                        print(err.args)
                    except Exception as ex:
                        print(ex.args)
                    else:
                        if item_type in [".par", ".psm"]:
                            replace_background(
                                doc, combine(template_path, PART))
                        elif item_type in [".asm"]:
                            replace_background(
                                doc, combine(template_path, ASSEMBLY))
                        elif item_type in [".pneu"]:
                            print(
                                "No views inside this draft, background can't be changed.")
                        else:
                            print("document unknown.")
